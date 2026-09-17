import pandas as pd

df = pd.read_csv("data/raw/dirty_order.csv", index_col = False)

# print(df)


# Print without the index column
print(df.to_string(index=False))

# Replace Nan with 0
df["amount"] = df["amount"].fillna(0)

# print(df)

# Convert float values into int
df["amount"] = df["amount"].astype(int)

print(df)


# Group By

country_summary = (
    df.groupby("country")
    .agg(
        total_orders=("order_id", "count"),total_amount=("amount","sum")
    )
)

print(country_summary)

# .cumsum() -> Running total of the amount (cummulative sum)
df["running_total"] = df["amount"].cumsum()
print(df)
