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
