from abc import ABC, abstractmethod


class TaskComponent(ABC):
    @abstractmethod
    def display(self):
        pass


class Task(TaskComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"{self.name}")


class TaskList(TaskComponent):
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display(self):
        for task in self.tasks:
            task.display()


if __name__ == "__main__":
    task1 = Task("Buy groceries")
    task2 = Task("Clean the house")
    task3 = Task("Pay bills")
    task4 = Task("Walk the dog")

    task3.display()
    print()

    sub_task_list = TaskList()
    sub_task_list.add_task(task1)
    sub_task_list.add_task(task2)

    sub_task_list.display()
    print()

    main_task_list = TaskList()
    main_task_list.add_task(task3)
    main_task_list.add_task(sub_task_list)
    main_task_list.add_task(task4)

    main_task_list.display()
