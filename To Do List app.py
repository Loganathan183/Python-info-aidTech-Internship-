import os
import json

def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return {}

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)

def show_menu():
    print("\nTodo List App")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks[len(tasks) + 1] = task
    print(f'Task "{task}" added successfully!')

def delete_task(tasks):
    print("Current Tasks:")
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if task_number in tasks:
        deleted_task = tasks.pop(task_number)
        print(f'Task "{deleted_task}" deleted successfully!')
    else:
        print("Invalid task number!")

def view_tasks(tasks):
    if tasks:
        print("\nCurrent Tasks:")
        for number, task in tasks.items():
            print(f"{number}. {task}")
    else:
        print("\nNo tasks available.")

def todo_list_app():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved successfully!")
        elif choice == '5':
            tasks = load_tasks()
            print("Tasks loaded successfully!")
        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved. Exiting the app.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    todo_list_app()
