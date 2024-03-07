# dataTask.py

import json

def save_to_json(tasks, filename):
    """Save a dictionary to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(tasks, f)

# Example usage:
tasks = {"Buy groceries": False, "Clean the kitchen": True}
save_to_json(tasks, "tasks.json")


def load_from_json(filename):
    """Load a dictionary from a JSON file."""
    with open(filename, 'r') as f:
        tasks = json.load(f)
    return tasks

# Example usage:
tasks = load_from_json("tasks.json")
print(tasks)

import os

def delete_database(filename):
    """Delete the database file."""
    if os.path.isfile(filename):
        os.remove(filename)
        print(f"File '{filename}' has been deleted.")
    else:
        print(f"File '{filename}' does not exist.")

# Example usage:
delete_database("tasks.json")
