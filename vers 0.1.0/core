"""модуль хранит главные функиии"""

from utils import check_confirm

def delete_task(task_collection):
    select_edit = input("Введите номер задачи для удаления: ")
    if check_confirm(select_edit, task_collection) == 1:
        edit_name = input("новое имч задачи")
        print(f"задача с номером {delete_task} успешно удалена")
        task_collection.pop(int(delete_task) - 1)

"""редактирует задачи"""
def edit_task(task_collection):
    edit_task = input("Введите номер задачи: ")
    if check_confirm(edit_task, task_collection):
        task_collection[int(edit_task) - 1] = input("Новое имя задачи: ")
    else:
        print("Неверный номер задачи!")

""""""
def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления: ")
    task_content = input("<UNK> <UNK> <UNK> <UNK> <UNK>: ")
    if task_name.startswith(" ") or task_name.endswith(" "):
        if len(task_content) < 2 or len(task_name) < 2:
            print("Название не может быть пустым")
            return
        else:
            task_collection.append(f"Задача {len(task_collection) + 1}")
    else:
        task_collection.append(task_name)
        print(f"Задача {task_name} успешно добавлена!")
