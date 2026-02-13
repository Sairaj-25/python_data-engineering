import csv

file = "data/raw/orders.csv"

with open(file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)