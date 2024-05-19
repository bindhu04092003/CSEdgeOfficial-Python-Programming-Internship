class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index!")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] += " (Completed)"
            print("Task marked as completed!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        else:
            print("No tasks to display!")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            try:
                task_index = int(input("Enter index of task to delete: ")) - 1
                todo_list.delete_task(task_index)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '3':
            try:
                task_index = int(input("Enter index of task to mark as completed: ")) - 1
                todo_list.mark_completed(task_index)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
