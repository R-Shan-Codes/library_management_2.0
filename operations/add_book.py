import data.store as store

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")

    store.books[book_id] = {
        "title": title,
        "available": True,
        "student": "",
        "days": 0
    }

    print("Book added successfully")