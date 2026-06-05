# Expense Tracker
# DecodeLabs Project 2

total_spent = 0
expenses = []

print("=" * 40)
print("      EXPENSE TRACKER")
print("=" * 40)

while True:

    expense = input(
        "\nEnter Expense Amount (or type 'done'): "
    )

    if expense.lower() == "done":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative.")
            continue

        expenses.append(expense)

        total_spent += expense

        print(f"Added: ₹{expense}")

    except ValueError:
        print("Please enter a valid number.")

print("\n" + "=" * 40)
print("Expense Summary")
print("=" * 40)

if len(expenses) == 0:
    print("No expenses entered.")
else:

    print("\nExpenses Entered:")

    for i, amount in enumerate(expenses, start=1):
        print(f"{i}. ₹{amount}")

    print("\nTotal Expenses:", len(expenses))
    print(f"Total Spent: ₹{total_spent:.2f}")

print("\nThank you for using Expense Tracker!")