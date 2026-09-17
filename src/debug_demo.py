def calculate_total(order):
    if "amount" not in order:
        raise ValueError("Missing 'amount' field")
    return order["amount"] * 2

# Spelling mistake of "amount" to raise error
order = {"amont":100}

print(calculate_total(order))