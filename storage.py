##===========================================================
##      Модуль который загружает и сохраняет задачи
##===========================================================
def save_tasks(task_collection, name_file):
    with open(name_file, "w", encoding="utf-8") as file:
        file.writelines(task_collection)

def load_tasks(name_file):
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []





def load_file(task_list,NAME_FILE_SAVES):
    with open(NAME_FILE_SAVES, "r", encoding="utf-8") as file:
        for line in file:
            task_list.append(line)
    return task_list


def save_file(task_list,NAME_FILE_SAVES):
    with open(NAME_FILE_SAVES, "w", encoding="utf-8") as file:
        file.write(f"{task_list}\n")






import tkinter as tk

root = tk.Tk()

root.geometry("300x300")
root.iconbitmap()

button_start = tk.Button(root, text="start")
button_start.pack()

root.mainloop()
