import requests

res = requests.get("https://jsonplaceholder.typicode.com/todos")
print(res.json())
print(type(res.json()))
for post in res.json():
    print(f"Post title: {post['title']}")