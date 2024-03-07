# taskDisplay.py

import os
from dataTask import load_from_json, save_to_json
from taskTool import add_task, remove_task, mark_task_complete

def main():
    print("Welcome to the task manager!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Load tasks")
        print("2. Create new tasks")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            filename = input("Enter the filename of the tasks JSON file: ")
            if os.path.isfile(filename):
                tasks = load_from_json(filename)
                display_tasks(tasks)
            else:
                print(f"File '{filename}' does not exist.")
        elif choice == "2":
            tasks = {}
            while True:
                print("\nWhat would you like to do?")
                print("1. Add a task")
                print("2. Remove a task")
                print("3. Mark a task as complete")
                print("4. Save tasks and exit")
                choice = input("Enter 1, 2, 3, or 4: ")
                if choice == "1":
                    task = input("Enter a task to add: ")
                    add_task(tasks, task)
                elif choice == "2":
                    task = input("Enter a task to remove: ")
                    remove_task(tasks, task)
                elif choice == "3":
                    task = input("Enter a task to mark as complete: ")
                    mark_task_complete(tasks, task)
                elif choice == "4":
                    filename = input("Enter the filename to save the tasks to: ")
                    save_to_json(tasks, filename)
                    print(f"Tasks saved to '{filename}'.")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
        else:
            print("Invalid choice. Please enter 1 or 2.")

def display_tasks(tasks):
    """Display the current tasks."""
    print("\nCurrent tasks:")
    for task, completed in tasks.items():
        status = "[ ]" if not completed else "[x]"
        print(f"{status} {task}")

if __name__ == "__main__":
    main()


