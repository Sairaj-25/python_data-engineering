import csv

rows = [
    ["order_id", "customer", "amount", "country"], 
    [1, "Alice", 120.5, "US"],
    [2, "Bob", 75.0, "IN"],
    [3, "Charlie", 200.0, "US"]
]

# If I run this file in root directory then the csv file is created in root.

# Common method to save csv in other folder location

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent 

# parent -> src/
# parent.parent -> python-de-project/

SAVE_DIR = BASE_DIR / "data" / "raw"  
# (OR {no need of BASE_DIR}) SAVE_DIR = Path("D:/Python/Python for data engineer/python-de-project/data/raw")

SAVE_DIR.mkdir(parents=True, exist_ok=True)

with open(SAVE_DIR/ "orders.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(rows)


# Professional method (Best for production/servers)


