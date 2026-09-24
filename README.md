# Expense Tracker CLI

A simple and beginner-friendly command-line expense tracker built with Python.  
It allows users to record expenses, view saved transactions, and generate category-wise monthly spending summaries.

## Features

- Add expenses with amount and category
- Validate invalid or negative expense amounts
- Prevent empty categories
- Automatically save the current date for each expense
- List all saved expenses
- Display the overall expense total
- Generate monthly, category-wise expense summaries
- Store expense records locally in a JSON file
- Simple command-line interface

## Technologies Used

- Python 3
- JSON for local data storage
- `datetime` module for date handling

## Project Structure

```text
expense-tracker/
├── main.py
├── README.md
├── .gitignore
└── expenses.json
```

> `expenses.json` is created automatically when you add your first expense.  
> It is recommended to keep this file in `.gitignore` because it may contain personal spending data.

## Requirements

Before running this project, make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

## Installation

1. Clone the repository:

```bash
git clone [https://github.com/YOUR-USERNAME/expense-tracker.git](https://github.com/YOUR-USERNAME/expense-tracker.git)
```

2. Move into the project directory:

```bash
cd expense-tracker
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment.

### Windows Git Bash

```bash
source .venv/Scripts/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
source .venv/bin/activate
```

5. Run the application:

```bash
python main.py
```

## Usage

When the application starts, it shows the following prompt:

```text
Command (add/list/summary/quit):
```

Available commands:

| Command | Description |
|---|---|
| `add` | Add a new expense |
| `list` | Display all saved expenses and the overall total |
| `summary` | Show a category-wise summary for a selected month |
| `quit` | Exit the application |

## Example

### Add an expense

```text
Expense Tracker CLI

Command (add/list/summary/quit): add
Enter amount (e.g. 500.75): 250
Enter category (e.g. Food, Transport, Rent): Food
Expense added successfully.
```

### List expenses

```text
Command (add/list/summary/quit): list

All expenses:
1. 2026-09-24 | Food | Rs. 250.00
2. 2026-09-24 | Transport | Rs. 150.00

Overall total: Rs. 400.00
```

### Monthly summary

```text
Command (add/list/summary/quit): summary
Enter month (YYYY-MM) or press Enter for the current month: 2026-09

Summary for 2026-09:
Food: Rs. 250.00
Transport: Rs. 150.00

Overall total for 2026-09: Rs. 400.00
```

## Data Format

Expenses are saved in the `expenses.json` file.

Example record:

```json
[
  {
    "amount": 250.0,
    "category": "Food",
    "description": "",
    "date": "2026-09-24"
  }
]
```

## Validation

The program checks the following:

- Expense amount must be a valid number.
- Expense amount must be greater than zero.
- Category cannot be empty.
- Monthly summary input must follow the `YYYY-MM` format.
- The month value must be between `01` and `12`.

## Future Improvements

- Add an optional description for each expense
- Allow users to enter a custom expense date
- Edit an existing expense
- Delete an expense
- Filter expenses by category
- Add a budget limit and overspending alert
- Export expense data to CSV
- Build a graphical user interface or web version

## Author

**Ali Mustanser**

## License

This project is for learning and educational purposes.
