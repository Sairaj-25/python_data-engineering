import csv

file = "/home/sairaj/Desktop/DISK/Python/Python for data engineer/python-de-project/data/raw/orders.csv"

with open(file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)