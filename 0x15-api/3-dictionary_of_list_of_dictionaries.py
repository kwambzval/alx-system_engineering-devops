#!/usr/bin/python3
"""
This module retrieves user data and their tasks from the JSONPlaceholder API
and exports the data into a JSON file. The data is organized by user ID with
each user's tasks listed, including task completion status and task title.
The output JSON file is named 'todo_all_employees.json'.

Usage:
    python3 script_name.py
"""

import requests
import json


def fetch_data(api_url):
    """
    Fetches data from the given API URL.

    Args:
        api_url (str): The URL of the API to fetch data from.

    Returns:
        dict: The response data from the API.
    """
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def get_users(api_url):
    """
    Retrieves user data from the API.

    Args:
        api_url (str): The URL of the API to fetch user data from.

    Returns:
        dict: A dictionary where each key is a user ID and each
        value is the user data.
    """
    return {user['id']: user['username'] for user in fetch_data(api_url)}


def get_tasks(api_url):
    """
    Retrieves task data from the API.

    Args:
        api_url (str): The URL of the API to fetch task data from.

    Returns:
        list: A list of dictionaries where each dictionary represents a task.
    """
    return fetch_data(api_url)


def organize_tasks_by_user(tasks, users):
    """
    Organizes tasks by user ID, including the task details.

    Args:
        tasks (list): A list of tasks where each task is a dictionary.
        users (dict): A dictionary of users where the key is the user ID and
        the value is the username.

    Returns:
        dict: A dictionary where each key is a user ID and each
        value is a list of task dictionaries.
    """
    tasks_by_user = {}
    for task in tasks:
        user_id = task['userId']
        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []
        tasks_by_user[user_id].append({
            'username': users[user_id],
            'task': task['title'],
            'completed': task['completed']
        })
    return tasks_by_user


def save_to_json(data, filename):
    """
    Saves the data to a JSON file.

    Args:
        data (dict): The data to save.
        filename (str): The name of the file to save the data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    """
    Main function that fetches user and task data, organizes it, and
    saves it to a JSON file.
    """
    user_api_url = 'https://jsonplaceholder.typicode.com/users'
    task_api_url = 'https://jsonplaceholder.typicode.com/todos'

    users = get_users(user_api_url)
    tasks = get_tasks(task_api_url)
    tasks_by_user = organize_tasks_by_user(tasks, users)
    save_to_json(tasks_by_user, 'todo_all_employees.json')


if __name__ == "__main__":
    main()
