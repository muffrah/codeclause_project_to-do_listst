# Creating an empty list to store the to-do items
todo_list = []

# Function to add a task to the to-do list
def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added successfully!")

# Function to remove a task from the to-do list
def remove_task():
    task = input("Enter the task to remove: ")
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the list.")

# Function to display the to-do list
def display_tasks():
    if todo_list:
        print("To-Do List:")
        for task in todo_list:
            print("- " + task)
    else:
        print("No tasks in the list.")

# Main program loop
while True:
    print("\n===== To-Do List Manager =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")