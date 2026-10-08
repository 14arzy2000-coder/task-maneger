"""Модуль для утилит"""
import sys
import os


def check_confirm(select_task, task_list):
    """Проверяет, что введён существующий номер задачи"""
    if select_task.isdigit():
        if 0 < int(select_task) <= len(task_list):
            return True
        else:
            print(f"Задачи с номером {select_task} нет в списке!")
            return False
    else:
        print("Введите именно номер задачи!")
        return False


def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


def insure_saves_file(name_file):
    """Создаёт файл сохранений, если его нет"""
    if not os.path.exists(name_file):
        with open(name_file, 'w', encoding="utf-8") as f:
            f.write("")
