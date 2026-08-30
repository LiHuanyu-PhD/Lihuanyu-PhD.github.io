import os
import re
import json
import time
import html as html_lib
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


SCHOLAR_ID = os.environ["GOOGLE_SCHOLAR_ID"]

PROFILE_URL = (
    "https://scholar.google.com/citations"
    f"?user={SCHOLAR_ID}&hl=en&pagesize=100"
)

TIMEOUT = 30
MAX_RETRIES = 3


def fetch_html(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close",
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(
                f"[Scholar] Fetching profile "
                f"({attempt}/{MAX_RETRIES})...",
                flush=True
            )

            request = Request(url, headers=headers)

            with urlopen(request, timeout=TIMEOUT) as response:
                page = response.read().decode(
                    "utf-8",
                    errors="ignore"
                )

            lower_page = page.lower()

            if (
                "unusual traffic" in lower_page
                or "captcha" in lower_page
                or "/sorry/" in lower_page
                or "not a robot" in lower_page
            ):
                raise RuntimeError(
                    "Google Scholar returned an anti-bot page."
                )

            print(
                f"[Scholar] Downloaded {len(page)} bytes.",
                flush=True
            )

            return page

        except (HTTPError, URLError, TimeoutError, RuntimeError) as e:
            print(
                f"[Scholar] Attempt failed: {e}",
                flush=True
            )

            if attempt < MAX_RETRIES:
                print(
                    "[Scholar] Retrying in 10 seconds...",
                    flush=True
                )
                time.sleep(10)

    raise RuntimeError(
        "Failed to fetch Google Scholar profile."
    )


def clean_text(value):
    value = re.sub(r"<[^>]+>", "", value)
    value = html_lib.unescape(value)
    return value.strip()


def parse_profile(page):
    author = {
        "updated": datetime.now().astimezone().isoformat(),
        "publications": {}
    }

    # Author name
    name_match = re.search(
        r'<div id="gsc_prf_in"[^>]*>(.*?)</div>',
        page,
        re.S
    )

    if name_match:
        author["name"] = clean_text(
            name_match.group(1)
        )

    # Citation / h-index / i10-index
    stats = re.findall(
        r'<td class="gsc_rsb_std">(\d+)</td>',
        page
    )

    if len(stats) < 5:
        raise RuntimeError(
            "Could not parse Scholar citation statistics."
        )

    author["citedby"] = int(stats[0])
    author["hindex"] = int(stats[2])
    author["i10index"] = int(stats[4])

    # Publications
    rows = re.findall(
        r'<tr class="gsc_a_tr">(.*?)</tr>',
        page,
        re.S
    )

    print(
        f"[Scholar] Found {len(rows)} publications.",
        flush=True
    )

    for row in rows:
        title_match = re.search(
            r'<a[^>]*class="gsc_a_at"[^>]*href="([^"]+)"[^>]*>'
            r'(.*?)</a>',
            row,
            re.S
        )

        if not title_match:
            continue

        href = html_lib.unescape(
            title_match.group(1)
        )

        title = clean_text(
            title_match.group(2)
        )

        pub_id_match = re.search(
            r'citation_for_view=([^&"]+)',
            href
        )

        if not pub_id_match:
            continue

        pub_id = pub_id_match.group(1)

        citation_match = re.search(
            r'<a[^>]*class="gsc_a_ac[^"]*"[^>]*>'
            r'\s*(\d*)\s*</a>',
            row,
            re.S
        )

        num_citations = 0

        if citation_match and citation_match.group(1):
            num_citations = int(
                citation_match.group(1)
            )

        year_match = re.search(
            r'class="gsc_a_h[^"]*"[^>]*>\s*(\d{4})\s*<',
            row,
            re.S
        )

        year = (
            int(year_match.group(1))
            if year_match
            else None
        )

        author["publications"][pub_id] = {
            "author_pub_id": pub_id,
            "bib": {
                "title": title
            },
            "num_citations": num_citations,
            "pub_year": year,
        }

    return author


def save_results(author):
    os.makedirs(
        "results",
        exist_ok=True
    )

    with open(
        "results/gs_data.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            author,
            f,
            ensure_ascii=False,
            indent=2
        )

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author["citedby"])
    }

    with open(
        "results/gs_data_shieldsio.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            shieldio_data,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[Scholar] Total citations: {author['citedby']}",
        flush=True
    )

    print(
        f"[Scholar] h-index: {author['hindex']}",
        flush=True
    )

    print(
        f"[Scholar] Publications: "
        f"{len(author['publications'])}",
        flush=True
    )

    print(
        "[Scholar] JSON files saved successfully.",
        flush=True
    )


def main():
    print(
        "[Scholar] Starting direct HTML crawler...",
        flush=True
    )

    page = fetch_html(
        PROFILE_URL
    )

    author = parse_profile(
        page
    )

    save_results(
        author
    )

    print(
        "[Scholar] Finished successfully.",
        flush=True
    )


if __name__ == "__main__":
    main()
