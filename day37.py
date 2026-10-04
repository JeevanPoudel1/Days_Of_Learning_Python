def show_menu():
    """Prints the user menu."""
    print("\n--- 📝 TASK MANAGER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks(tasks):
    """Displays all current tasks and their status."""
    if not tasks:
        print("\nYour task list is empty!")
        return

    print("\nYour Tasks:")
    for index, (task, status) in enumerate(tasks.items(), start=1):
        icon = "✅" if status else "❌"
        print(f"{index}. [{icon}] {task}")


def add_task(tasks):
    """Adds a new task to the list."""
    task_name = input("\nEnter the task name: ").strip()
    if task_name:
        if task_name in tasks:
            print("That task already exists!")
        else:
            tasks[task_name] = False  # False means incomplete
            print(f"Added: '{task_name}'")
    else:
        print("Task name cannot be empty.")


def complete_task(tasks):
    """Marks a selected task as completed."""
    if not tasks:
        print("\nNo tasks to complete!")
        return

    view_tasks(tasks)
    task_list = list(tasks.keys())

    try:
        choice = int(input("\nEnter the number of the task you completed: "))
        if 1 <= choice <= len(task_list):
            selected_task = task_list[choice - 1]
            tasks[selected_task] = True
            print(f"Great job! Marked '{selected_task}' as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    """Removes a task from the list."""
    if not tasks:
        print("\nNo tasks to delete!")
        return

    view_tasks(tasks)
    task_list = list(tasks.keys())

    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        if 1 <= choice <= len(task_list):
            selected_task = task_list[choice - 1]
            del tasks[selected_task]
            print(f"Removed: '{selected_task}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main loop to run the application."""
    # Using a dictionary where key = task name, value = completion status (True/False)
    tasks = {
        "Buy groceries": False,
        "Read a book chapter": True,
    }

    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye! Stay productive! 👋")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")


# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
