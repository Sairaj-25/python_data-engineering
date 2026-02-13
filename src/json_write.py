import json

data = {
    "orders": [
        {"id":1, "item":[{"name":"apple", "price":100, "unit":"kg"}], "quantity":10},
        {"id":2, "item":[{"name":"banana", "price":40, "unit":"dozen"}], "quantity":5},
        {"id":3, "item":[{"name":"orange", "price":50, "unit":"kg"}], "quantity":8},
        {"id":4, "item":[{"name":"grape", "price":80, "unit":"kg"}], "quantity":12}
    ]
}

file = "data/raw/orders.json"

with open(file, "w") as f:
    json.dump(data, f, indent=2) # json.dump convert : Dictionary to JSON string and write it to file. indent=2 is used to make the JSON file more readable by adding indentation.