Expense Tracker

A lightweight Python CLI tool to log and track your expenses.
Records are stored in a local CSV file (SQLite backend planned).

Features

Add expenses with category, description, and amount

Store records in a CSV file

View total spending by category

View monthly summaries (with optional --month YYYY-MM)

Cross-platform (Windows, macOS, Linux)

Example Usage
# Add expenses
python tracker.py add --amount 12.50 --category food --desc "Lunch"
python tracker.py add --amount 800 --category rent --desc "October rent"

# Show summary by category
python tracker.py summary

# Show all months grouped by category
python tracker.py monthly

# Filter by specific month
python tracker.py monthly --month 2025-09

Roadmap

[x] Basic CSV storage

[x]CLI flags with argparse (add, summary, monthly)

[ ] Switch to SQLite backend

[ ] Export charts with Matplotlib or Pandas

Quick Start

Clone the repository and set up a virtual environment:

Linux / macOS
git clone 
cd expense-tracker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tracker.py --help

Windows (PowerShell)
git clone 
cd expense-tracker
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python tracker.py --help

Windows (CMD)
git clone 
cd expense-tracker
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
python tracker.py --help

Requirements

Python 3.8+

Pandas (for summaries)