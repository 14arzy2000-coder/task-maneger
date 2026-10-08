"""Модуль, который отображает вид"""


def show_collection(task_collection):
    """Показывает список задач (только название, до символа '|')"""
    print("=" * 30)
    for number, content in enumerate(task_collection, start=1):
        name = content.split("|")[0]
        print(number, name)
    print("=" * 30)


def show_menu():
    """Показывает меню"""
    print("1 - Показать задачи \n"
          "2 - Добавить задачу \n"
          "3 - Редактировать задачу \n"
          "4 - Удалить задачу \n"
          "5 - Выход")
