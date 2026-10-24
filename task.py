import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


tasks = load_tasks()

while True:
    print("\n===== SMART TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ").strip()

        if task:
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print("Task added successfully!")
        else:
            print("Task cannot be empty!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, start=1):
                status = "Done" if item["done"] else "Pending"
                print(f"{i}. {item['task']} [{status}]")

    elif choice == "3":
        try:
            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["done"] = True
                save_tasks(tasks)
                print("Task completed!")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        try:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                save_tasks(tasks)
                print("Deleted:", removed["task"])
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "5":
        print("Goodbye! Tasks saved.")
        break

    else:
        print("Invalid choice!")