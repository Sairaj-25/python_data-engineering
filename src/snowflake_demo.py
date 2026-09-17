import os
import snowflake.connector
from dotenv import load_dotenv
load_dotenv()

# Configure the connecion 

conn = snowflake.connector.connect(
    account= os.getenv("SNOWFLAKE_ACCOUNT"),
    user= os.getenv("SNOWFLAKE_USER"),
    password= os.getenv("SNOWFLAKE_PASSWORD"),
    # "authenticator":"externalbrowser",
    role= os.getenv("SNOWFLAKE_ROLE"),
    warehouse= os.getenv("SNOWFLAKE_WAREHOUSE"),
    database= os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")   
)

# Opena a Cursor 
cursor = conn.cursor()

# Execute a Query
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER,
    amount INTEGER,
    country STRING
    )
    """
)

# Insert data in the table 
"""
cursor.execute() -> is for one set of parameters 

cursor.executemany() -> to insert list of values   =>   [(101, 500, "IN"),(102, 750, "USA"),(103, 1200, "UK"),(104, 300, "CAN"),]
"""

try:
    cursor.execute(
        """
        INSERT INTO orders(order_id, amount, country)
        VALUES (%s,%s,%s)
        """,
        (102, 600, "USA")
    )
    print("Insert successful")

except Exception as e:
    print("Insert Failed:",e)


# fetch DATa from table
cursor.execute(
    "SELECT order_id, amount, country FROM orders"
)
rows = cursor.fetchall()

print("Extraction Successful")

for row in rows:
    print(row)


# Don't forget to close the connection

cursor.close()
conn.close()
