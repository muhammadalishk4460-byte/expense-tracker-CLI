import json
from datetime import date

DATA_FILE = "expenses.json"
def load_expenses():
    try:
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            data = json.load(f)
            if isinstance (data,list):
                return data
            return []
    except(FileNotFoundError,json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(expenses,f,ensure_ascii=False,indent=2)

def add_expense(expenses):
    while True:
        amount_str = input("enter amount(e.g. 500.75): ").strip()
        try:
            amount = float(amount_str)
            if amount<=0:
                print("amount should be greater than 0.")
                continue
            break
        except(ValueError):
            print("invalid error: please enter a number like 100 or 500.75")
    while True:
        category = input("enter category(e.g. food,transport,rent): ").strip()
        if category:
            break
        print("category cannot be empty.")
    expense = {
            "amount":amount,
            "category":category,
            "description":"",
            "date":date.today().isoformat()
        }
    expenses.append(expense)
    print("Expense added succesfully(amount + category for now.)")
def list_expenses(expenses):
    if not expenses:
        print("no expenses.")
        return
    print("\nAll Expenses: ")
    for i,exp in enumerate(expenses,start=1):
        amount = exp.get("amount",0)
        category = exp.get("category", "")
        when = exp.get("date","")
        print(f"{i} . {when} | {category} | Rs. {amount:.2f}")  

def monthly_summary(expenses):
    if not expenses:
        print("no expenses found.")
        return
    while True:
        month_str = input("enter month (YYYY-MM) or press enter for the current month: ").strip()
        if not month_str:
            today = date.today()
            month_str = today.strftime("%Y-%m")
            break
        try:
            year,month = map(int,month_str.split("-"))
            if not (1 <= month <= 12):
                raise ValueError
            if year<1900 or year>2100:
                raise ValueError
            break
        except(ValueError):
            print("invalid format , use (YYYY-MM) e.g (2025-09).")

        month_expense =[
            e for e in expenses
            if e.get("date","").startswith(month_str)]
        if not month_expense:
            print(f"no expenses for {month_str}")
            return
        print(f"\n Summary for {month_str}: ")
        total_expenses ={}
        for e in month_expense:
            cat = e.get("category","uncategoried")
            amt = e.get("amount",0)
            total_expenses[cat] = total_expenses.get(cat,0) + amt
        for cat, total in total_expenses.items():
            print(f"{cat} : Rs. {total:.2f}")

        overall_total = sum(total_expenses.values())
        print(f"\n Overall total for {month_str}: Rs. {overall_total:.2f}")  
def main():
    expenses = load_expenses()
    print("expense tracker CLI")
    while True:
        cmd = input("command (add/list/summary/quit): ").strip().lower()
        if cmd == "add":
            add_expense(expenses)
            save_expenses(expenses)
        elif cmd == "list":
            list_expenses(expenses)
        elif cmd == "summary":
            monthly_summary(expenses)
        elif cmd == "quit":
            break
        else:
            print("unknown command.")
if __name__=="__main__":
    main()