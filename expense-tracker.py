# expense-tracker.py
import pandas as pd
import argparse
from pathlib import Path
import datetime

# still just using csv, maybe add sqlite later
DATA_FILE = Path("expenses.csv")


def load_data():
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["date", "amount", "category", "description"])


def save_data(df):
    df.to_csv(DATA_FILE, index=False)


def add_expense(amount, category, description):
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


def monthly_report(month=None):
    df = load_data()
    if df.empty:
        print("No data yet for monthly report.")
        return

    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")

    if month:
        # note: no validation yet
        df = df[df["month"] == month]

    report = df.groupby(["month", "category"])["amount"].sum()
    print("\n--- Monthly Report ---")
    print(report)


def main():
    parser = argparse.ArgumentParser(description="Simple expense tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", type=str, required=True)
    add_parser.add_argument("--desc", type=str, default="")

    # summary command
    subparsers.add_parser("summary", help="Show expense summary")

    # monthly report command
    monthly_parser = subparsers.add_parser("monthly", help="Show monthly report")
    monthly_parser.add_argument("--month", type=str, help="e.g. 2025-09")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.amount, args.category, args.desc)
    elif args.command == "summary":
        show_summary()
    elif args.command == "monthly":
        monthly_report(args.month)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
