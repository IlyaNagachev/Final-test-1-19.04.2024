import json
import os
import datetime

notes_file = "notes.json"

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    with open(notes_file, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

def add_note():
    notes = load_notes()
    id = len(notes) + 1
    title = input("Напишите название заметки: ")
    body = input("Напишите содержание заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": id, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена успешно.")

def read_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Timestamp: {note['timestamp']}")
        print()

def edit_note():
    notes = load_notes()
    id = int(input("Введите номер заметки для изменения: "))
    for note in notes:
        if note["id"] == id:
            note["title"] = input("Введите новое название: ")
            note["body"] = input("Введите новое содержание: ")
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка изменена успешно.")
            return
    print("Заметка не найдена.")

def delete_note():
    notes = load_notes()
    id = int(input("Введите номер заметки для удаления: "))
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена успешно.")
            return
    print("Заметка не найдена.")

while True:
    print("\n1. Добавить заметку\n2. Прочитать заметку\n3. Изменить заметку\n4. Удалить заметку\n5. Выйти")
    choice = input("Введите число действия: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
