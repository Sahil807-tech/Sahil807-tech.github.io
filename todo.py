tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Added: {task}")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        num = input("Enter task number to delete: ")
        if num.isdigit() and 1 <= int(num) <= len(tasks):
            removed = tasks.pop(int(num) - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
