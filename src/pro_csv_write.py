# Professional method (Best for production/servers)

import csv
import os
from pathlib import Path

rows = [
    ["order_id", "customer", "amount", "country"],
    [1, "Alice", 120.5, "US"],
    [2, "Bob", 75.0, "IN"],
    [3, "Charlie", 200.0, "US"]
]


# Read env variable

# SAVE_DIR = os.getenv("CSV_OUTPUT_DIR")

# Read environment variable (STRICT)
SAVE_DIR = Path(os.environ["CSV_OUTPUT_DIR"])

SAVE_DIR.mkdir(parents=True, exist_ok=True)

# command to setup env variables in cmd
#1 set CSV_OUTPUT_DIR=D:\python-de-data\raw (Temporary (current CMD session only)➡️ Works only in this Command Prompt window ➡️ Close CMD = variable gone)
#-#-# Verify:----- echo %CSV_OUTPUT_DIR%


#2 setx CSV_OUTPUT_DIR "D:\python-de-data\raw" (Permanent (Windows-wide, survives restart)➡️ Takes effect in new CMD windows only)
#-#-# Verify (open a NEW CMD)::----- echo %CSV_OUTPUT_DIR%


with open(SAVE_DIR / "orders_env.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)



r""" 
Option A — Temporary (must be in SAME CMD)
open cmd or terminal(cmd) -->

--Move to the correct drive 
C:\Users\hp>D: 

cd "D:\Python\Python for data engineer\python-de-project"
set CSV_OUTPUT_DIR=D:\Python\Python for data engineer\python-de-project\data\raw
echo %CSV_OUTPUT_DIR%
python src\professional_csv.py

"""