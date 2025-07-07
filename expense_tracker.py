# expense_tracker.py

def main():
    print("💸 Expense Tracker")
    date = input("Date (YYYY-MM-DD): ")
    amount = input("Amount: ")
    category = input("Category: ")
    note = input("Note (optional): ")

    print("\nEntry recorded:")
    print(f"{date} | ${amount} | {category} | {note}")

if __name__ == "__main__":
    main()
