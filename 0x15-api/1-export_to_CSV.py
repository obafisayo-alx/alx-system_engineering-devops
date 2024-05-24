#!/usr/bin/python3
"""exports a csv file with inputs gotten from an api"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the user provided a user ID as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    # Get the user ID from the command line arguments
    user_id = int(sys.argv[1])

    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user = user_response.json()

    # Fetch todos for the user
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create the CSV filename
    filename = f"{user_id}.csv"

    # Write todos to the CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow(
                [
                    user_id,
                    user['username'],
                    todo['completed'],
                    todo['title']
                ]
            )

    # print(f"Data exported to {filename}")