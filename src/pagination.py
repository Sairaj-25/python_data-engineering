import requests

page = 1

all_data = []

while True:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1",
        params={"_page":page, "_limits":5}
    )

    if not response.json():
        break

    all_data.extend(response.json())
    page+=1

print(len(all_data))