from config import NAME_FILE_SAVES
from utils import insure_saves_file
from view import show_collection, show_menu
from storage import load_file, save_file
from core import add_task, edit_task, delete_task


def app():
    is_running = True
    name_file = NAME_FILE_SAVES
    insure_saves_file(name_file)
    task_collection = load_file([], name_file)  # загружаем один раз, до цикла

    while is_running:
        show_menu()
        choice_user = input("Ваш выбор: ")

        match choice_user:
            case "1":
                show_collection(task_collection)
                input("Нажмите ENTER для продолжения")

            case "2":
                task_collection = add_task(task_collection)
                save_file(task_collection, name_file)

            case "3":
                show_collection(task_collection)
                edit_task(task_collection)
                save_file(task_collection, name_file)

            case "4":
                show_collection(task_collection)
                delete_task(task_collection)
                save_file(task_collection, name_file)

            case "5":
                is_running = False
                print("До свидания!")

            case _:
                print("Такого пункта нет...")
