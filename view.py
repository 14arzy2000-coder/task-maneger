"""модуль который отображает вид"""

"""загрузка списка задач"""

def show_collection(task_collection):
    print("=" * 30)
    for number, content in enumerate(task_collection):
        word = ''
        for symbol in content:
            if symbol != '|':
                word = f'{word}{symbol}'
            else:
                break
            print(number + 1, str(word))
    print("=" * 30)

"""функция для показа списка задач"""
def show_menu():
    print("1 - Показать задачи \n"
          "2 - Добавить задачу \n"
          "3 - Редактировать задачи \n"
          "4 - Удаление задачи \n"
          "5 - Выход")
