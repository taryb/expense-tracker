import pandas as pd
from pathlib import Path
import datetime

DATA_FILE = Path("expenses.csv")

def load_data():
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["date", "amount", "category", "description"])

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")
    description = input("Description: ")
    date = datetime.date.today().isoformat()

    df = load_data()
    new_row = {"date": date, "amount": amount, "category": category, "description": description}
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

def main():
    while True:
        print("\n1) Add expense\n2) Show summary\n3) Quit")
        choice = input("> ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
