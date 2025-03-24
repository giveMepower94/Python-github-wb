import os
# Напишите функцию, которая создает заметку


def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(f"Заметка с названием {note_name} создана!")


# Напишите функцию, которая запрашивает название и текст заметки у пользователя, после чего создает заметку

def crete_note():
    note_name = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")

    build_note(note_text, note_name)


# Напишите функцию, которая выводит заметку по запросу пользователя

def read_note():
    try:
        note_name = input("Введите название заметки: ")
        if os.path.isfile(note_name):
            print("Файл существует")
            with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
                file.read()
        else:
            print("Заметка не найдена")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Напишите функцию, которая редактирует заметку

def edit_note():
    try:
        note_name = input("Введите название заметки: ")
        if os.path.isfile(note_name):
            print("Файл существует")
            with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
                file.read()

            new_content = input("Введите новый текст заметки: ")
            with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
                file.write(new_content)
                print("Заметка успешно обновлена.")
        else:
            print("Заметка не найдена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")