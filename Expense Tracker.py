'''Expense Tracker'''

import os
import json
from datetime import datetime

# File to store expense data
DATA_FILE = "expenses.json"

# Initialize data storage
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

# Function to load expense data
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Function to save expense data
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Function to add an expense
def add_expense():
    try:
        date_input = input("Enter the date (DD-MM-YYYY): ")
        date = datetime.strptime(date_input, "%d-%m-%Y").strftime("%d-%m-%Y")
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")

        data = load_data()
        if date not in data:
            data[date] = []

        data[date].append({
            "category": category,
            "amount": amount,
            "description": description
        })
        save_data(data)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to view all expenses
def view_expenses():
    data = load_data()
    if not data:
        print("No expenses recorded yet.")
        return

    print("\nExpense Data:")
    for date, expenses in data.items():
        print(f"\nDate: {date}")
        for expense in expenses:
            print(f"  Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

# Function to view monthly summaries
def monthly_summary():
    data = load_data()
    if not data:
        print("No expenses recorded yet.")
        return

    monthly_totals = {}
    for date, expenses in data.items():
        month = "-".join(date.split("-")[1:])  # Extract MM-YYYY
        if month not in monthly_totals:
            monthly_totals[month] = 0
        monthly_totals[month] += sum(expense['amount'] for expense in expenses)

    print("\nMonthly Summary:")
    for month, total in monthly_totals.items():
        print(f"  {month}: {total:.2f}")

# Function to view category-wise expenditure
def category_summary():
    data = load_data()
    if not data:
        print("No expenses recorded yet.")
        return

    category_totals = {}
    for expenses in data.values():
        for expense in expenses:
            category = expense['category']
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += expense['amount']

    print("\nCategory-wise Summary:")
    for category, total in category_totals.items():
        print(f"  {category}: {total:.2f}")

# Menu-driven interface
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_expense()
            elif choice == '2':
                view_expenses()
            elif choice == '3':
                monthly_summary()
            elif choice == '4':
                category_summary()
            elif choice == '5':
                print("Thank you for using the Expense Tracker!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
