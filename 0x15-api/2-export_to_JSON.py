#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports data
in JSON format.
"""
import json
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
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
            )
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a list of tasks
    tasks = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks.append(task_dict)

    # Create the final dictionary
    data = {str(employee_id): tasks}

    # File name
    file_name = "{}.json".format(employee_id)

    # Write to JSON file
    with open(file_name, mode='w') as file:
        json.dump(data, file)
