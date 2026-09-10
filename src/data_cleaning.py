import csv
from pathlib import Path


# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Input file
INPUT_FILE = BASE_DIR / "data" / "raw" / "messy_orders.csv"

# Output file
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "clean_messy_orders.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


clean_orders = []


with open(INPUT_FILE, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # Remove extra spaces from customer name
        customer = row["customer"].strip()

        # Convert email to lowercase
        email = row["email"].strip().lower()

        # Convert amount from string to float
        amount = float(row["amount"])

        # Convert country to uppercase
        country = row["country"].strip().upper()

        # Skip record if customer name is empty
        if not customer:
            print("Skipping record because customer name is missing")
            continue

        clean_orders.append(
            {
                "order_id": row["order_id"],
                "customer": customer,
                "email": email,
                "amount": amount,
                "country": country,
            }
        )


# Write cleaned data
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["order_id", "customer", "email", "amount", "country"],
    )

    writer.writeheader()
    writer.writerows(clean_orders)


print(f"Raw file: {INPUT_FILE}")
print(f"Clean file: {OUTPUT_FILE}")
print(f"Records processed: {len(clean_orders)}")
