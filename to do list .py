class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} - {status}")
        else:
            print("No tasks available.")

    def mark_task_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed.")
        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(
                input("Enter the index of the task to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
