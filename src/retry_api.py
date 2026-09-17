import time
# import requests

retries = 3

for attempt in range(retries):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        response.raise_for_status()
        print("request successful")
        break
    except Exception as e:
        print(f"Attempt {attempt+1} Failed:{e}")
        time.sleep(2)