tasks = []

def display_tasks():
    print("Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['name']} - {status}")

def add_task(new_task):
    task = {"name": new_task, "completed": False}
    tasks.append(task)
    print(f"Task '{new_task}' added successfully.")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task['name']}' removed successfully.")
    else:
        print("Invalid task index.")

def mark_completed(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Task marked as completed.")
    else:
        print("Invalid task index.")

while True:
    print("\nOptions:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as completed")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        new_task = input("Enter the new task: ")
        add_task(new_task)
    elif choice == '3':
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == '4':
        task_index = int(input("Enter the task index to mark as completed: "))
        mark_completed(task_index)
    elif choice == '5':
        print("Exiting the to-do list.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")