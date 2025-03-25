import os
# Напишите функцию, которая создает заметку


def build_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
            file.write(note_text)
            print(f"Заметка с названием {note_name} создана!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



# Напишите функцию, которая запрашивает название и текст заметки у пользователя, после чего создает заметку

def create_note():
    try:
        note_name = input("Введите название заметки: ")
        note_text = input("Введите текст заметки: ")

        build_note(note_text, note_name)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


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

# Напишите функцию, которая удаляет заметку


def delete_note():
    try:
        note_name = input("Введите название заметки: ")
        if os.path.isfile(note_name):
            os.remove(note_name)
            print("Заметка успешно удалена.")
        else:
            print("Заметка не найдена.")

    except Exception as e:
        print(f"Произошла ошибка при удалении заметки: {e}")

# Напишите функцию, которая управляет работой приложения


def main():
    while True:
        print('\nМеню')
        print('1. Создать заметку')
        print('2. Прочитать заметку')
        print('3. Отредактировать заметку')
        print('4. Удалить заметку')
        print('5. Демонстрация заметок в упорядоченном виде')

        choice = input('Выберите действие (1/2/3/4/5): ')

        if choice == 1:
            create_note()
        elif choice == 2:
            read_note()
        elif choice == 3:
            edit_note()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            display_notes()
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из меню.")

# Напишите функцию, которая выводит все заметки пользователя


def display_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith(".txt")]

        notes_sorted = sorted(notes, key=lambda note: len(open(note, encoding='utf-8').read()))

        for note in notes_sorted:
            with open(note, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"\nСодержимое заметки '{note}':")
                print(content)
    except Exception as e:
        print(f"Произошла ошибка при отображении заметок: {e}")