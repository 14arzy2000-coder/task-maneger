"""модуль который отображает вид


print("=" * 30)
    for number, content in enumerate(collection):
        word = ''
        for symbol in content:
            if symbol != '|':
                word = f'{word}{symbol}'
            else:
                break
"""
from storage import load_file, save_file
from config import NAME_FILE_SAVES
from ui.Interface import interface
collection = load_file([], NAME_FILE_SAVES)
ui = interface()

def menu():
        show_all_tasks()

def show_all_tasks():

    for number, content in enumerate(collection):
        print(f'{number}. {content}')
        ui.list_task.add_to_list(content["name"])
        ui.list_box.bind("<<ListboxSelect>>", show_all_tasks())

    def delete:
        cur_task = ui.list_box.curselection()
        collection[cur_task[0]]
        print(task)


main()
ui.root.mainloop()


