import json

file = "data/raw/orders.json"

with open(file, "r") as f:
    data = json.load(f) # json.load convert : JSON string from file to Python Dictionary. It reads the JSON data from the file and parses it into a Python dictionary.

# for order in data["orders"]:
#     print(order)



# convert json data(clumsy) to flattened dictionary
rows = []

for order in data["orders"]:
    for item in order["item"]:
        rows.append({
            "order_id":order["id"],
            "product": item["name"],
            "price": item["price"],
            "unit": item["unit"],
            "qty": order["quantity"]
        })

print(rows)