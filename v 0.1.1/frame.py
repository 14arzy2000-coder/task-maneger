import tkinter as tk

class AppFrame():
    def __init__(self, master, color, width, height):
        super().__init__(master, bg=color, width=width, height=height)
        self.background = color
        self.master = master
        self.width = width
        self.height = height
        self.pack_propagate(False)
        self.pack()
        self.text = text

    def hide(self, event: bool):
        if event: self.pack.forget()
        else: self.pack()
