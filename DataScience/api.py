import requests
r = requests.get('https://jsonplaceholder.typicode.com/todos/1', auth=('user', 'pass'))
print(r.json())