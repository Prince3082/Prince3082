expenses = []

def add_expense():
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = input("Enter amount: ")
    date = input("Enter date (YYYY-MM-DD): ")

    if not amount.isdigit():
        print("Invalid amount! Please enter a number.")
        return

    expense = {
        "category": category.title(),
        "amount": int(amount),
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses to show.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - Rs.{exp['amount']} - {exp['date']}")
    print()

def search_expense():
    if not expenses:
        print("No data available.\n")
        return

    category = input("Enter category to search: ").title()
    found = False

    print(f"\nExpenses in category: {category}")
    for exp in expenses:
        if exp["category"] == category:
            print(f"- Rs.{exp['amount']} on {exp['date']}")
            found = True

    if not found:
        print("No expenses found in this category.\n")
    else:
        print()

def total_spent():
    if not expenses:
        print("No expenses recorded.\n")
        return

    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spending so far: Rs.{total}\n")

def save_to_file():
    filename = input("Enter filename to save (e.g. data.txt): ")
    with open(filename, "w") as f:
        for exp in expenses:
            f.write(f"{exp['category']},{exp['amount']},{exp['date']}\n")
    print(f"Expenses saved to {filename}\n")

def load_from_file():
    filename = input("Enter filename to load (e.g. data.txt): ")
    try:
        with open(filename, "r") as f:
            for line in f:
                category, amount, date = line.strip().split(",")
                expenses.append({
                    "category": category,
                    "amount": int(amount),
                    "date": date
                })
        print(f"Data loaded from {filename}\n")
    except FileNotFoundError:
        print("File not found. Please check the filename.\n")
    except Exception as e:
        print(f"Error loading file: {e}\n")

def main():
    while True:
        print("""
=== SMART EXPENSE TRACKER ===
1. Add Expense
2. View All Expenses
3. Search by Category
4. Show Total Spending
5. Save to File
6. Load from File
7. Exit
""")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expense()
        elif choice == "4":
            total_spent()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            print("Thank you for using Smart Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
