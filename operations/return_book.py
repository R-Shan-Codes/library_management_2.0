import data.store as store

def calculate_fine(extra_days):
    fine = 0

    for day in range(1, extra_days + 1):
        week = (day - 1) // 7 + 1
        rate = 10

        for i in range(1, week + 1):
            rate *= i   # increasing pattern

        fine += rate

    return fine


def return_book():
    book_id = input("Enter Book ID: ")

    if book_id not in store.books:
        print("Book not found")
        return

    book = store.books[book_id]

    if book["available"]:
        print("Book was not issued")
        return

    used_days = int(input("Enter how many days you kept the book: "))
    allowed_days = book["days"]

    print(f"Allowed: {allowed_days} days | Used: {used_days} days")

    if used_days > allowed_days:
        extra = used_days - allowed_days
        fine = calculate_fine(extra)
        print(f"Late by {extra} days → Fine = ₹{fine}")
    else:
        print("Returned on time. No fine")

    # reset
    book["available"] = True
    book["student"] = ""
    book["days"] = 0

    print("Book returned successfully")