class Task:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "Задача: " + self.name

    def get_type(self):
        return "Обычная задача"


class StudyTask(Task):
    def show_info(self):
        return "Учеба: " + self.name

    def get_type(self):
        return "Учебная задача"


class HomeTask(Task):
    def show_info(self):
        return "Домашнее дело в доме: " + self.name

    def get_type(self):
        return "Домашняя задача"
