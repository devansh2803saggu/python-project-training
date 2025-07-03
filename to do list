def display_todos(todos):
    if not todos:
        print("\nNo tasks in the list.\n")
        return
    print("\nYour To-Do List:")
    for i, (task, done) in enumerate(todos, 1):
        status = "[x]" if done else "[ ]"
        print(f"{i}. {status} {task}")
    print()

def main():
    todos = []
    while True:
        print("Menu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            display_todos(todos)

        elif choice == '2':
            task = input("Enter the task: ").strip()
            if task:
                todos.append((task, False))
                print(f"Added task: {task}\n")
            else:
                print("Task cannot be empty.\n")

        elif choice == '3':
            display_todos(todos)
            if todos:
                try:
                    task_num = int(input("Enter the number of the task to mark done: "))
                    if 1 <= task_num <= len(todos):
                        task, _ = todos[task_num-1]
                        todos[task_num-1] = (task, True)
                        print(f"Marked task #{task_num} as done.\n")
                    else:
                        print("Invalid task number.\n")
                except ValueError:
                    print("Please enter a valid number.\n")

        elif choice == '4':
            display_todos(todos)
            if todos:
                try:
                    task_num = int(input("Enter the number of the task to delete: "))
                    if 1 <= task_num <= len(todos):
                        task, _ = todos.pop(task_num-1)
                        print(f"Deleted task: {task}\n")
                    else:
                        print("Invalid task number.\n")
                except ValueError:
                    print("Please enter a valid number.\n")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
