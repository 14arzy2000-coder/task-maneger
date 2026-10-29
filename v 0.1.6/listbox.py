
import tkinter as tk


class AppListbox(tk.Listbox):
    def __init__(self, master):
        super().__init__(master, width=40, height=10)
        self.pack(pady=10)

    def add_to_list(self, content):
        self.insert(tk.END, content)

    def delete_list(self):
        selected = self.curselection()

        if selected:
            self.delete(selected[0])
            return selected[0]

        return None
