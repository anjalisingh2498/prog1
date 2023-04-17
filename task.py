class Task:
    def __init__(self, name, priority, deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.completed = False

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

class TaskManager:
    def __init__(self):
        self.projects = []

    def create_project(self, name):
        project = Project(name)
        self.projects.append(project)

    def add_task_to_project(self, project_name, task):
        for project in self.projects:
            if project.name == project_name:
                project.add_task(task)

    def get_tasks_by_priority(self, priority):
        tasks = []
        for project in self.projects:
            for task in project.get_tasks():
                if task.priority == priority:
                    tasks.append(task)
        return tasks

    def get_tasks_by_deadline(self, deadline):
        tasks = []
        for project in self.projects:
            for task in project.get_tasks():
                if task.deadline == deadline:
                    tasks.append(task)
        return tasks

    def get_incomplete_tasks(self):
        tasks = []
        for project in self.projects:
            for task in project.get_tasks():
                if not task.completed:
                    tasks.append(task)
        return tasks

    def mark_task_as_completed(self, task_name):
        for project in self.projects:
            for task in project.get_tasks():
                if task.name == task_name:
                    task.completed = True

# Example usage
tm = TaskManager()
tm.create_project("Project 1")
tm.add_task_to_project("Project 1", Task("Task 1", "High", "2023-05-01"))
tm.add_task_to_project("Project 1", Task("Task 2", "Medium", "2023-06-01"))
tm.create_project("Project 2")
tm.add_task_to_project("Project 2", Task("Task 3", "Low", "2023-07-01"))
tm.add_task_to_project("Project 2", Task("Task 4", "High", "2023-08-01"))
print("Tasks with high priority:")
for task in tm.get_tasks_by_priority("High"):
    print(task.name)
print("Tasks with deadline on 2023-07-01:")
for task in tm.get_tasks_by_deadline("2023-07-01"):
    print(task.name)
print("Incomplete tasks:")
for task in tm.get_incomplete_tasks():
    print(task.name)
tm.mark_task_as_completed("Task 1")
print("Incomplete tasks after marking Task 1 as completed:")
for task in tm.get_incomplete_tasks():
    print(task.name)
