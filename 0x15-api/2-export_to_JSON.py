#!/usr/bin/python3
"""export data in json format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])
    req_url0 = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    users = requests.get(req_url0).json()

    req_url1 = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    todos = requests.get(req_url1).json()

    tasks = []
    for todo in todos:
        tasks.append({
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': users.get('username')
        })
    filename = f'{user_id}.json'
    with open(filename, mode='w') as file:
        json.dump({user_id: tasks}, file)
