# Expense Tracker

A simple Python CLI tool to log and track your expenses.  
Records are stored in a local CSV file (or SQLite later), and you can generate summaries by category or date.

## Features
- Add expenses with category, description, and amount
- Store records in a CSV file
- View total spending by category
- View monthly summaries
- Cross-platform (Windows, macOS, Linux)

## Roadmap
- [x] Basic CSV storage
- [ ] Switch to SQLite backend
- [ ] CLI flags (e.g. `--add`, `--summary`)
- [ ] Export charts with Matplotlib or Pandas

## Quick Start

Clone the repository and set up a virtual environment:

### Linux / macOS
```bash
git clone
cd expense-tracker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python expense_tracker.py


###POWERSHELL
git clone
cd expense-tracker
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python expense_tracker.py


###CMD

git clone 
cd expense-tracker
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
python expense_tracker.py
