import  tkinter as tk
from frame import AppFrame


class Interface:
    def __init__(self, window_w=400, window_h=400):
        self.root = tk.Tk()
        self.root_w = window_w
        self.root_h = window_h
        self.root.geometry(f"{self.root_w}x{self.root_h}")


        self.frames = []
        self.buttons = []

        self.create_interface()

        self.root.mainloop()
        self.create_frames(["menu", "tasks"])
        self.create_buttons()
        self.create_buttons2()


    def create_frames(self, name_frame):
        c = ["black","grey"]
        for i in range(len(name_frame)):
            frame = AppFrame(frame, c[i], self.root_w, self.root_h)
            self.frames[name_frame[i]] = frame

    def create_buttons(self):
        button_show_tasks = tk.Button(self.frames["menu"], color="blue", text="посмотреть все задачи")
        button_show_tasks.pack()
        button_show_tasks2 = tk.Button(self.frames["tasks"], color="green", text="назад к задачам")
        button_show_tasks2.pack()

    def create_interface(self):
        pass


interface = Interface()
