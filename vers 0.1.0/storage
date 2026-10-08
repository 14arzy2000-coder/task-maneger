def load_file(task_list, file_name):
    """Читает задачи из файла и добавляет их в список"""
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:  # пропускаем пустые строки
                task_list.append(line)
    return task_list


def save_file(task_list, file_name):
    """Записывает все задачи в файл"""
    with open(file_name, "w", encoding="utf-8") as file:
        for task in task_list:
            file.write(f"{task}\n")
