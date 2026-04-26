import data.store as store

def issue_book():
    book_id = input("Enter Book ID: ")

    if book_id not in store.books:
        print("Book not found")
        return

    book = store.books[book_id]

    if not book["available"]:
        print("Book already issued")
        return

    name = input("Enter Student Name: ")
    days = int(input("For how many days: "))

    book["available"] = False
    book["student"] = name
    book["days"] = days

    print("Book issued successfully")
    print(f"Return within {days} days to avoid fine")