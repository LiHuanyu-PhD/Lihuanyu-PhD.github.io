import os
import json
from datetime import datetime
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


SCHOLAR_ID = os.environ["GOOGLE_SCHOLAR_ID"]
SERPAPI_KEY = os.environ["SERPAPI_KEY"]

API_URL = "https://serpapi.com/search.json"
TIMEOUT = 60


def get_scholar_data():
    print("[Scholar] Fetching data from SerpApi...", flush=True)

    params = {
        "engine": "google_scholar_author",
        "author_id": SCHOLAR_ID,
        "hl": "en",
        "num": 100,
        "api_key": SERPAPI_KEY,
    }

    url = API_URL + "?" + urlencode(params)

    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            data = json.loads(
                response.read().decode("utf-8")
            )

    except HTTPError as e:
        raise RuntimeError(
            f"SerpApi HTTP error: {e.code}"
        )

    except URLError as e:
        raise RuntimeError(
            f"SerpApi connection error: {e}"
        )

    if "error" in data:
        raise RuntimeError(
            f"SerpApi error: {data['error']}"
        )

    status = data.get(
        "search_metadata", {}
    ).get("status")

    if status and status != "Success":
        raise RuntimeError(
            f"SerpApi search status: {status}"
        )

    print(
        "[Scholar] SerpApi request successful.",
        flush=True
    )

    return data


def parse_data(data):

    result = {
        "updated": datetime.now().astimezone().isoformat(),
        "publications": {}
    }

    # =========================
    # Author information
    # =========================
    author_info = data.get("author", {})

    result["name"] = author_info.get(
        "name",
        ""
    )

    # =========================
    # Citation statistics
    # =========================
    cited_by = data.get(
        "cited_by",
        {}
    )

    table = cited_by.get(
        "table",
        []
    )

    total_citations = 0
    h_index = 0
    i10_index = 0

    for item in table:

        if "citations" in item:
            total_citations = (
                item["citations"].get(
                    "all",
                    0
                )
            )

        if "h_index" in item:
            h_index = (
                item["h_index"].get(
                    "all",
                    0
                )
            )

        if "i10_index" in item:
            i10_index = (
                item["i10_index"].get(
                    "all",
                    0
                )
            )

    result["citedby"] = total_citations
    result["hindex"] = h_index
    result["i10index"] = i10_index

    # =========================
    # Publications
    # =========================
    articles = data.get(
        "articles",
        []
    )

    print(
        f"[Scholar] Found {len(articles)} publications.",
        flush=True
    )

    for article in articles:

        citation_id = article.get(
            "citation_id"
        )

        if not citation_id:
            continue

        cited_by_info = article.get(
            "cited_by",
            {}
        )

        num_citations = cited_by_info.get(
            "value",
            0
        )

        title = article.get(
            "title",
            ""
        )

        authors = article.get(
            "authors",
            ""
        )

        publication = article.get(
            "publication",
            ""
        )

        year = article.get(
            "year"
        )

        result["publications"][citation_id] = {
            "author_pub_id": citation_id,
            "bib": {
                "title": title,
                "author": authors,
                "citation": publication,
            },
            "num_citations": num_citations,
            "pub_year": year,
        }

    return result


def save_results(author):

    os.makedirs(
        "results",
        exist_ok=True
    )

    # Main JSON
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

    # Shields.io JSON
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(
            author["citedby"]
        ),
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
        "[Scholar] Starting SerpApi crawler...",
        flush=True
    )

    data = get_scholar_data()

    author = parse_data(data)

    save_results(author)

    print(
        "[Scholar] Finished successfully.",
        flush=True
    )


if __name__ == "__main__":
    main()
