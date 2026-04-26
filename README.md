# 📚 Library Management System

A simple Library Management System built in Python using a modular structure and dictionary-based storage.

---

## 📌 Features

* 📖 Add new books
* 📋 View all books
* 👤 Issue book with student name and days
* 🔁 Return book
* 💰 Fine calculation for late return
* 📦 Modular structure (services, models, utils)
* 📋 Menu-driven program (`while True` loop)

---

## 🧠 How It Works

* Books are stored using a dictionary

* Each book has:

  * Title
  * Availability status
  * Issued student name
  * Number of days issued

* While issuing:

  * User enters student name and number of days

* While returning:

  * User enters how many days the book was used
  * If exceeded → fine is applied

---

## 💰 Fine Rules

* Week 1 → ₹10 per day
* Week 2 → ₹20 per day
* Week 3 → ₹60 per day
* Continues in increasing pattern

---

## 📁 Project Structure

```
library/
│
├── main.py
├── operations/
│   ├── add_book.py
│   ├── show_books.py
│   ├── issue_book.py
│   └── return_book.py
│
├── data/
    └── (store.py)
```

---

## ▶️ How to Run

1. Open terminal in project folder
2. Run:

```
python main.py
```

---

## 🕹️ Menu Options

* 1 → Add Book
* 2 → Show Books
* 3 → Issue Book
* 4 → Return Book
* 5 → Exit

---
