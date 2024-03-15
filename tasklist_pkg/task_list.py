import datetime

last_id = 0


class Task:
    """
    Task: it is the class to generate task object with title and description attributes and
          match method as action.
    """

    def __init__(self, title, description):
        global last_id
        last_id += 1
        self.id = last_id
        self.title = title
        self.description = description
        self.status = True
        self.creation_date = datetime.date.today()

    def match(self, filterTxt):
        """
        match(str): uses to ensure that the text filter is match any task or not
        :param filterTxt: the word which is used to find specific task
        :return: boolean
        """
        return filterTxt in self.title or filterTxt in self.description

    def status_toggle(self):
        """
        status_toggle(): which is used to change the status of task inverse the current status.
        :return: boolean
        """
        self.status = not self.status


class TaskList:
    """
    TaskList is a class uses to generate object contains list of task with various actions such as
    search task , add task, modify and remove specific task.
    """

    def __init__(self):
        self.tasklist = []

    def _find_task(self, task_id):
        for task in self.tasklist:
            if task.id == task_id:
                return task
        return None

    def search_task(self, search_keyword):
        """
        This function,simply, takes string parameter to search it inside list of tasks
        :param search_keyword: string parameter uses to return list of matched tasks.
        :return: list of tasks
        """
        locatedTasks = []
        for task in self.tasklist:
            if task.match(search_keyword):
                locatedTasks.append(task)
        return locatedTasks

    def new_task(self, title, desc):
        """
        Create new task
        :param title: string data type, the title of task
        :param desc: string data type, the description of the task
        :return: void
        """
        self.tasklist.append(Task(title, desc))

    def modify_title(self, task_id, new_title):
        """
        This method uses to update the value of task title based on given task id
        :param task_id: string data type, the id of given task
        :param new_title: the new value which should use instead of old value of title
        :return: void
        """
        self._find_task(task_id).title = new_title

    def modify_description(self, task_id, new_desc):
        """
            This method uses to update the value of task description based on given task id
            :param task_id: string data type, the id of given task
            :param new_desc: the new value which should use instead of old value of description
            :return: void
        """
        self._find_task(task_id).description = new_desc

    def active_tasks(self):
        """
           This method uses to get all tasks their statuses are True
           :return: list of task
        """
        return [task for task in self.tasklist if task.status]

    def complete_tasks(self):
        """
          This method uses to get all tasks their statuses are False
          :return: list of task
        """
        return [task for task in self.tasklist if not task.status]
