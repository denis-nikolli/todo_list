tasks = []

while True:
    print("\nWhat would you like to do?")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            index = int(input("Enter the task number to delete: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1–4.")

