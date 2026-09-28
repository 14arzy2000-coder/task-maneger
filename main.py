"""Основной файл приложения

    версия 0.0.7.

    === Описание ===
        Приложение может сохранять задачи, выдает список задач, и может удалять и редактировать задачи

"""
from fff import delete_task
from view import show_collection, show_menu
from storage import load_file, save_file
from core import add_task, edit_task

is_running = True


def main():
    global is_running
    global name_file
    name_file = NAME_FILE_SAVE
    while is_running:
        show_menu()
        choice_user = input("vas vibor")
        task_collection = load_file(name_file)


        match str(choice_user):
            case "1":
                show_collection(task_collection)
                input("нажмите ENTER для продолжения")

            case "2":
                task_collection = add_task(task_collection)
                save_file(name_file, task_collection)

            case "3":
                show_collection(task_collection)
                edit_task(task_collection)

            case "4":
                show_collection(task_collection)
                delete_task(task_collection)

            case "5":
                is_running = False
                print("До свидиния!")

            case _:
                print('Такого пункта нет...')
                is_running = True

  
