tasks = []
task_id_counter = 1

def add_task():
    global task_id_counter
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    if title and description:
        task = {
            'id': task_id_counter,
            'title': title,
            'description': description
        }
        tasks.append(task)
        task_id_counter += 1
        print("Task added successfully!")
    else:
        print("Invalid input. Task not added.")

def edit_task():
    task_id = int(input("Enter task ID to edit: ").strip())
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        title = input(f"Enter new title (current: {task['title']}): ").strip()
        description = input(f"Enter new description (current: {task['description']}): ").strip()
        if title:
            task['title'] = title
        if description:
            task['description'] = description
        print("Task updated successfully!")
    else:
        print("Task not found.")

def delete_task():
    task_id = int(input("Enter task ID to delete: ").strip())
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    print("Task deleted successfully!")

def list_tasks():
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")
    else:
        print("No tasks available.")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            edit_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
