#!/usr/bin/python3
"""Using Api get todo list of an employee"""
import requests
from sys import argv


def todos(user_id):
    EMP_NAME = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(user_id)).json()["name"]
    TASKS = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                            .format(user_id)).json()
    TASKS_COMPLETED = ['\t {}\n'.format(res.get('title')) for res in TASKS
                 if res.get('completed')]
    NUMBER_OF_DONE_TASKS = (len(TASKS_COMPLETED))
    TOTAL_NUMBER_OF_TASKS = (len(TASKS))
    print("Employee {} is done with tasks({}/{}):"
          .format(EMP_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    print(''.join(TASKS_COMPLETED), end='')

if __name__ == "__main__":
    if len(argv) == 2:
        todos(int(argv[1]))
