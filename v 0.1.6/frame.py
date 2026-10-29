import tkinter as tk


class AppFrame(tk.Frame):
    def __init__(self, master, color, width, height):
        super().__init__(
            master,
            bg=color,
            width=width,
            height=height
        )

        self.pack_propagate(False)
        self.pack(fill="both", expand=True)

    def hide(self, event):
        if event:
            self.pack_forget()
        else:
            self.pack(fill="both", expand=True)
