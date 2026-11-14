
from csv_manager import CSVManager


class ExpenseManager:

    def __init__(self):
        self.expenses = CSVManager.load_expenses()

    # 1. Add Expense with duplicate ID validation
    
    def add_expense(self, expense):

        self.expenses = CSVManager.load_expenses()

        new_id = str(expense.expense_id).strip()

        # Check duplicate Expense ID
        for existing_expense in self.expenses:
            if new_id == str(existing_expense.expense_id).strip():
                print("Error: Expense ID already exists!")
                return

        # Validate category
        if not str(expense.category).strip():
            print("Error: Category cannot be empty!")
            return

        # Validate amount
        try:
            amount = float(expense.amount)

            if amount <= 0:
                print("Error: Amount must be greater than zero!")
                return

        except (ValueError, TypeError):
            print("Error: Please enter a valid amount!")
            return

        # Validate description
        if not str(expense.description).strip():
            print("Error: Description cannot be empty!")
            return

        # Save valid expense
        expense.amount = amount
        self.expenses.append(expense)

        CSVManager.save_expenses(self.expenses)

        print("Expense added successfully!")


    # 2. View All Expenses
    def view_expenses(self):

        self.expenses = CSVManager.load_expenses()

        print("\n========== ALL EXPENSES ==========")

        if not self.expenses:
            print("No expenses available!")
            return

        print("Total Expense Records:", len(self.expenses))

        for expense in self.expenses:
            print("\n----- EXPENSE DETAILS -----")
            print("Expense ID:", expense.expense_id)
            print("Trip ID:", expense.trip_id)
            print("Category:", expense.category)
            print("Amount:", expense.amount)
            print("Description:", expense.description)

    # 3. Calculate Total Expenses
    def total_expenses(self):

        self.expenses = CSVManager.load_expenses()

        total = 0

        for expense in self.expenses:
            total += float(expense.amount)

        return total

    # 4. Calculate Expenses for a Particular Trip
    def trip_total_expenses(self, trip_id):

        self.expenses = CSVManager.load_expenses()

        total = 0

        for expense in self.expenses:

            if str(expense.trip_id).strip() == str(trip_id).strip():
                total += float(expense.amount)

        return total

    # 5. Update Expense
    def update_expense(self, expense_id):

        self.expenses = CSVManager.load_expenses()

        expense = None

        for item in self.expenses:
            if str(item.expense_id).strip() == str(expense_id).strip():
                expense = item
                break

        if expense is None:
            print("Expense not found!")
            return

        print("\n----- UPDATE EXPENSE -----")

        category = input("Enter New Category: ").strip()
        amount = float(input("Enter New Amount: "))
        description = input("Enter New Description: ").strip()

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        expense.category = category
        expense.amount = amount
        expense.description = description

        CSVManager.save_expenses(self.expenses)

        print("Expense updated successfully!")

    # 6. Delete Expense
    def delete_expense(self, expense_id):

        self.expenses = CSVManager.load_expenses()

        expense = None

        for item in self.expenses:
            if str(item.expense_id).strip() == str(expense_id).strip():
                expense = item
                break

        if expense is None:
            print("Expense not found!")
            return

        confirmation = input(
            "Are you sure you want to delete this expense? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":

            self.expenses.remove(expense)

            CSVManager.save_expenses(self.expenses)

            print("Expense deleted successfully!")

        else:
            print("Delete operation cancelled!")
