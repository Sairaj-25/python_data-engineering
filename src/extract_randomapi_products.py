"""Fetch RandomAPI.dev ecommerce products and save a 5 MB raw JSON file.

Purpose: create a simple source file for the Snowflow S3 -> Snowflake pipeline.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

import requests

API_URL = "https://randomapi.dev/api/products"
OUTPUT_DIR = Path(
    "/home/sairaj/Desktop/DISK/Python/Python for data engineer/python-de-project/data/raw"
)
TARGET_BYTES = 5_000_000  # Exact file size used for S3/Snowflake testing.
BATCH_SIZE = 100  # API supports 1-100 records per request.
START_SEED = 20260914  # Fixed seed makes test data reproducible.


def fetch_batch(seed: int) -> list[dict]:
    """Fetch one batch from RandomAPI.dev."""
    response = requests.get(
        API_URL,
        params={
            "count": BATCH_SIZE,
            "seed": seed,
            "currency": "INR",
            "format": "json",
            "pretty": "false",
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["data"]


def json_bytes(products: list[dict], extracted_at: str) -> bytes:
    """Build compact JSON bytes; compact output saves storage and transfer cost."""
    payload = {
        "data": products,
        "meta": {
            "endpoint": "products",
            "source": "randomapi.dev",
            "extracted_at_utc": extracted_at,
            "record_count": len(products),
        },
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def main() -> None:
    """Fetch records until the JSON content is close to 5 MB, then pad safely."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    extracted_at = datetime.now(timezone.utc).isoformat()
    products: list[dict] = []
    seed = START_SEED

    # Add whole API batches first for efficient network usage.
    while len(json_bytes(products, extracted_at)) < TARGET_BYTES - 100_000:
        products.extend(fetch_batch(seed))
        seed += 1

    # Add records one at a time so the final JSON never exceeds the target.
    while True:
        next_record = fetch_batch(seed)[0]
        candidate = products + [next_record]
        if len(json_bytes(candidate, extracted_at)) > TARGET_BYTES:
            break
        products = candidate
        seed += 1

    # Valid JSON allows trailing whitespace, so spaces can safely reach exactly 5 MB.
    content = json_bytes(products, extracted_at)
    padding = TARGET_BYTES - len(content)
    output_file = OUTPUT_DIR / f"randomapi_products_raw_{datetime.now().strftime('%Y%m%d')}.json"
    output_file.write_bytes(content + (b" " * padding))

    print(f"Created: {output_file}")
    print(f"Records: {len(products):,}")
    print(f"Size:    {output_file.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
