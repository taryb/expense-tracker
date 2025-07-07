# expense_tracker.py

import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expense(entry):
    expenses = load_expenses()
    expenses.append(entry)
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
    print("✅ Expense saved to file!")

def main():
    print("💸 Expense Tracker")
    date = input("Date (YYYY-MM-DD): ")
    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note (optional): ")

    entry = {
        "date": date,
        "amount": amount,
        "category": category,
        "note": note
    }

    save_expense(entry)

if __name__ == "__main__":
    main()
