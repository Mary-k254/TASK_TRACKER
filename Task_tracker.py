import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task name: ")
    task = {"title": title, "done": False}
    tasks.append(task)
    print(f"✅ Task '{title}' added!")

def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. [{status}] {task['title']}")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"✅ Task '{tasks[index]['title']}' marked as complete.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n📋 Task Tracker Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("👋 Exiting. Tasks saved!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
