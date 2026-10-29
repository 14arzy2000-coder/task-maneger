import tkinter as tk

from button import AppButton
from listbox import AppListbox
from frame import AppFrame
from rod import Task, StudyTask, HomeTask

class Interface:
    def __init__(self, root):
        self.root = root
        self.collection = []

        self.frame = AppFrame(
            self.root,
            "white",
            400,
            450
        )

        self.label = tk.Label(
            self.frame,
            text="Мой список задач"
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.frame, width=30)
        self.entry.pack(pady=5)

        self.list_box = AppListbox(self.frame)

        self.button1 = AppButton(
            self.frame,
            "Добавить задачу",
            self.add_task
        )

        self.button2 = AppButton(
            self.frame,
            "Учебная задача",
            self.add_study_task
        )

        self.button3 = AppButton(
            self.frame,
            "Домашняя задача",
            self.add_home_task
        )

        self.button4 = AppButton(
            self.frame,
            "Удалить задачу",
            self.delete_task
        )

    def add_task(self):
        name = self.entry.get()

        if name != "":
            task = Task(name)
            self.collection.append(task)
            self.list_box.add_to_list(task.show_info())
            self.entry.delete(0, tk.END)

    def add_study_task(self):
        name = self.entry.get()

        if name != "":
            task = StudyTask(name)
            self.collection.append(task)
            self.list_box.add_to_list(task.show_info())
            self.entry.delete(0, tk.END)

    def add_home_task(self):
        name = self.entry.get()

        if name != "":
            task = HomeTask(name)
            self.collection.append(task)
            self.list_box.add_to_list(task.show_info())
            self.entry.delete(0, tk.END)

    def delete_task(self):
        number = self.list_box.delete_list()

        if number is not None:
            self.collection.pop(number)
