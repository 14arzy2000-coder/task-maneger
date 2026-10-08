"""Модуль хранит главные функции"""

from utils import check_confirm


def delete_task(task_collection):
    """Удаляет задачу по номеру"""
    select_task = input("Введите номер задачи для удаления: ")
    if check_confirm(select_task, task_collection):
        task_collection.pop(int(select_task) - 1)
        print(f"Задача с номером {select_task} успешно удалена")
    return task_collection


def edit_task(task_collection):
    """Редактирует название задачи, описание сохраняется"""
    select_task = input("Введите номер задачи: ")
    if check_confirm(select_task, task_collection):
        index = int(select_task) - 1
        new_name = input("Новое имя задачи: ").strip()
        if not new_name:
            print("Название не может быть пустым")
            return task_collection
        parts = task_collection[index].split("|", 1)
        description = parts[1] if len(parts) > 1 else ""
        task_collection[index] = f"{new_name}|{description}"
        print("Задача успешно изменена!")
    return task_collection


def add_task(task_collection):
    """Добавляет задачу в формате 'название|описание'"""
    task_name = input("Введите имя задачи для добавления: ").strip()
    if not task_name:
        print("Название не может быть пустым")
        return task_collection
    task_content = input("Введите описание задачи: ").strip()
    task_collection.append(f"{task_name}|{task_content}")
    print(f"Задача {task_name} успешно добавлена!")
    return task_collection
