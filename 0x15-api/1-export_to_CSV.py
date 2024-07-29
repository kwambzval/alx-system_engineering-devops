#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports data
in CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user data
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos data
    todos_url = (
            "https://shorturl.at/xmopn".format(employee_id)
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # File name
    file_name = "{}.csv".format(employee_id)

    # Write to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, username, task.get("completed"),
                             task.get("title")])
