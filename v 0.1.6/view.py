import tkinter as tk

from interface import Interface

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Мой список задач")
        self.root.geometry("400x450")

        self.interface = Interface(self.root)

    def show(self):
        self.root.mainloop()

view = View()
view.show()
