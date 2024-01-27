class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            print(f"- {task}")

if __name__ == "__main__":
    to_do_list = ToDoList()

    # Example Usage
    to_do_list.add_task("Complete Project A")
    to_do_list.add_task("Study for Exam")

    to_do_list.display_tasks()
