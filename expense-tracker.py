# tracker.py
import pandas as pd
from pathlib import Path
import datetime

# maybe config this later, just hardcoding for now
DATA_FILE = Path("expenses.csv")


def load_data():
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    else:
        # not sure if I should add types here
        return pd.DataFrame(columns=["date", "amount", "category", "description"])


def save_data(df):
    # TODO: add try/except later
    df.to_csv(DATA_FILE, index=False)


def add_expense():
    # TODO: maybe better to validate input later?
    amount = float(input("Amount: "))
    category = input("Category: ")
    description = input("Description: ")
    date = datetime.date.today().isoformat()

    df = load_data()
    new_row = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    print("Expense saved.")


def show_summary():
    df = load_data()
    if df.empty:
        print("No expenses recorded yet.")
        return
    summary = df.groupby("category")["amount"].sum()
    print("\n--- Expense Summary ---")
    print(summary)


def monthly_report():
    df = load_data()
    if df.empty:
        print("No data yet for monthly report.")
        return

    # quick hack, might improve later
    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")
    report = df.groupby(["month", "category"])["amount"].sum()
    print("\n--- Monthly Report ---")
    print(report)


def main():
    while True:
        print("\n1) Add expense\n2) Show summary\n3) Monthly report\n4) Quit")
        choice = input("> ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            monthly_report()
        elif choice == "4":
            break
        else:
            print("Invalid choice, lol.")  # maybe remove "lol" later


if __name__ == "__main__":
    main()
