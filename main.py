from operations.add_book import add_book
from operations.show_books import show_books
from operations.issue_book import issue_book
from operations.return_book import return_book

def menu():
    print("\n LIBRARY MENU")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

while True:
    menu()
    ch = input("Enter choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        show_books()
    elif ch == "3":
        issue_book()
    elif ch == "4":
        return_book()
    elif ch == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")