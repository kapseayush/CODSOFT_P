# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to update a task
def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_index] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted.")
        else:
            print("Invalid task number.")

# Main function
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
