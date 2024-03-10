import json
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, message):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": datetime.datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Сообщение: {note['message']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print()

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена.")

def filter_notes_by_date(date):
    notes = load_notes()
    filtered_notes = [note for note in notes if note['timestamp'].startswith(date)]
    for note in filtered_notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Сообщение: {note['message']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print()

def main():
    while True:
        print("1. Добавить заметку")
        print("2. Список заметок")
        print("3. Удалить заметку")
        print("4. Фильтрация заметок по дате")
        print("5. Выйти")
        
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            add_note(title, message)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "4":
            date = input("Введите дату для фильтрации (гггг-мм-дд): ")
            filter_notes_by_date(date)
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
