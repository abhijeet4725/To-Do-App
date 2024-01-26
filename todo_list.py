# Simple Todo List in Python

todos = []
index_counter = 1  # Variable to manually track index

while True:
    print("\n===== Todo App =====")
    print("1. Display Todos")
    print("2. Add Todo")
    print("3. Complete Todo")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("===== Todo List =====")
        for todo in todos:
            print(f"{index_counter}. {todo}")
            index_counter += 1
        print("=====================")
        index_counter = 1  # Reset index counter after displaying todos
    elif choice == '2':
        new_todo = input("Enter the new todo: ")
        todos.append(new_todo)
        print(f"Added: {new_todo}")
    elif choice == '3':
        if todos:
            index = int(input("Enter the index of the completed todo: "))
            if 1 <= index <= len(todos):
                completed_todo = todos.pop(index - 1)
                print(f"Completed: {completed_todo}")
            else:
                print("Invalid index")
        else:
            print("No todos to complete")
    elif choice == '4':
        print("Exiting Todo App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
