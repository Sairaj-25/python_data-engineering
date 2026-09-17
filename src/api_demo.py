import requests

url = "https://dummyjson.com/c/4dc9-0c44-464a-9f90"

response = requests.get(url)

data = response.json()

# print(data)

parsed = []

for post in data:
    parsed.append(
        {
            "order_id": post["order_id"],
            "order_status": post["order_status"],
            "customer_id": post["customer"]["customer_id"],
            "customer_name": (
                post["customer"]["first_name"]
                + " "
                + post["customer"]["last_name"]
            ),
            "payment_method": post["payment"]["payment_method"],
            "grand_total": post["pricing"]["grand_total"]
        }
    )

# print(parsed)
print(parsed[:2])