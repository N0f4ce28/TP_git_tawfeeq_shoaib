# taskTool.py
#Add words to dictionary

def add_task(tasks, task):
    """Add a new task to the tasks dictionary."""
    if task in tasks:
        print(f"Task '{task}' already exists.")
    else:
        tasks[task] = False
        print(f"Task '{task}' has been added.")

# Example usage:
tasks = {}
add_task(tasks, "Buy groceries")
add_task(tasks, "Clean the kitchen")
print(tasks)

#Remove words from dictionary

def remove_task(tasks, task):
    """Remove a task from the tasks dictionary."""
    if task in tasks:
        del tasks[task]
        print(f"Task '{task}' has been removed.")
    else:
        print(f"Task '{task}' does not exist.")

# Example usage:
tasks = {"Buy groceries": False, "Clean the kitchen": True}
remove_task(tasks, "Buy groceries")
print(tasks)

#Mark words from dictionary

def mark_task_complete(tasks, task):
    """Mark a task as complete in the tasks dictionary."""
    if task in tasks:
        tasks[task] = True
        print(f"Task '{task}' has been marked as complete.")
    else:
        print(f"Task '{task}' does not exist.")

# Example usage:
tasks = {"Buy groceries": False, "Clean the kitchen": True}
mark_task_complete(tasks, "Buy groceries")
print(tasks)

# taskDisplay.py

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
                    display_tasks(tasks)
                elif choice == "2":

