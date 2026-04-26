import data.store as store

def show_books():
    if not store.books:
        print("No books available")
        return

    print("\nBooks List:")
    for bid, info in store.books.items():
        status = "Available" if info["available"] else f"Issued to {info['student']}"
        print(f"{bid} - {info['title']} → {status}")