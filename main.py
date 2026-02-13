import json
import os
from datetime import datetime

FILENAME = "expenses.json"


def load_data():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def add_expense():
    data = load_data()

    title = input("Enter expense title: ").strip()
    category = input("Enter category (Food/Travel/etc): ").strip()

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(expense)
    save_data(data)
    print("Expense added successfully.")


def view_expenses():
    data = load_data()

    if not data:
        print("No expenses recorded.")
        return

    total = 0

    for i, exp in enumerate(data, start=1):
        print("\n--------------------------")
        print(f"Expense #{i}")
        print(f"Title    : {exp['title']}")
        print(f"Category : {exp['category']}")
        print(f"Amount   : {exp['amount']}")
        print(f"Date     : {exp['date']}")
        print("--------------------------")
        total += exp["amount"]

    print(f"\nTotal Spending: {total}")


def delete_expense():
    data = load_data()

    if not data:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        index = int(input("Enter expense number to delete: "))
        if 1 <= index <= len(data):
            removed = data.pop(index - 1)
            save_data(data)
            print(f"Deleted expense: {removed['title']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
  #Add expense tracker main program
