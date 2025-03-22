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