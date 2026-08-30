from scholarly import scholarly
import json
from datetime import datetime
import os
import sys
import time
import signal


# =========================
# Configuration
# =========================
MAX_RETRIES = 3
SEARCH_TIMEOUT = 60       # seconds
FILL_TIMEOUT = 120        # seconds
RETRY_INTERVAL = 15       # seconds


class ScholarTimeoutError(Exception):
    pass


def timeout_handler(signum, frame):
    raise ScholarTimeoutError("Google Scholar request timed out.")


signal.signal(signal.SIGALRM, timeout_handler)


def run_with_timeout(func, timeout, *args, **kwargs):
    """Run a scholarly function with a timeout."""
    signal.alarm(timeout)

    try:
        result = func(*args, **kwargs)
        signal.alarm(0)
        return result
    except Exception:
        signal.alarm(0)
        raise


def fetch_scholar_data(author_id):
    """Fetch Google Scholar profile with retries."""

    for attempt in range(1, MAX_RETRIES + 1):

        try:
            print(
                f"[Scholar] Attempt {attempt}/{MAX_RETRIES}",
                flush=True
            )

            # Step 1: Search author
            print(
                f"[Scholar] Searching author ID: {author_id}",
                flush=True
            )

            author = run_with_timeout(
                scholarly.search_author_id,
                SEARCH_TIMEOUT,
                author_id
            )

            if not author:
                raise RuntimeError(
                    "Google Scholar author profile was not found."
                )

            print(
                f"[Scholar] Author found: {author.get('name', 'Unknown')}",
                flush=True
            )

            # Step 2: Fetch full profile
            print(
                "[Scholar] Fetching citations and publications...",
                flush=True
            )

            author = run_with_timeout(
                scholarly.fill,
                FILL_TIMEOUT,
                author,
                sections=[
                    'basics',
                    'indices',
                    'counts',
                    'publications'
                ]
            )

            print(
                "[Scholar] Google Scholar data fetched successfully.",
                flush=True
            )

            return author

        except ScholarTimeoutError as e:
            print(
                f"[Scholar] Timeout: {e}",
                flush=True
            )

        except Exception as e:
            print(
                f"[Scholar] Error: {type(e).__name__}: {e}",
                flush=True
            )

        if attempt < MAX_RETRIES:
            print(
                f"[Scholar] Retrying in {RETRY_INTERVAL} seconds...",
                flush=True
            )
            time.sleep(RETRY_INTERVAL)

    raise RuntimeError(
        f"Failed to fetch Google Scholar data after "
        f"{MAX_RETRIES} attempts."
    )


def main():

    # =========================
    # Scholar ID
    # =========================
    author_id = os.environ.get('GOOGLE_SCHOLAR_ID')

    if not author_id:
        print(
            "[Error] GOOGLE_SCHOLAR_ID is not configured.",
            flush=True
        )
        sys.exit(1)

    print(
        "[Scholar] Starting Google Scholar crawler...",
        flush=True
    )

    try:
        author = fetch_scholar_data(author_id)

    except Exception as e:
        print(
            f"[Fatal] {e}",
            flush=True
        )
        sys.exit(1)

    # =========================
    # Process profile
    # =========================
    author['updated'] = datetime.now().astimezone().isoformat()

    publications = author.get('publications', [])

    author['publications'] = {
        pub['author_pub_id']: pub
        for pub in publications
        if 'author_pub_id' in pub
    }

    citedby = author.get('citedby', 0)

    print(
        f"[Scholar] Total citations: {citedby}",
        flush=True
    )

    print(
        f"[Scholar] Publications: {len(author['publications'])}",
        flush=True
    )

    # =========================
    # Save results
    # =========================
    os.makedirs('results', exist_ok=True)

    gs_file = 'results/gs_data.json'

    with open(gs_file, 'w', encoding='utf-8') as outfile:
        json.dump(
            author,
            outfile,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[Scholar] Saved: {gs_file}",
        flush=True
    )

    # =========================
    # Shields.io JSON
    # =========================
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citedby),
    }

    shield_file = 'results/gs_data_shieldsio.json'

    with open(shield_file, 'w', encoding='utf-8') as outfile:
        json.dump(
            shieldio_data,
            outfile,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[Scholar] Saved: {shield_file}",
        flush=True
    )

    print(
        "[Scholar] Finished successfully.",
        flush=True
    )


if __name__ == '__main__':
    main()
