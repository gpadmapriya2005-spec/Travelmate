class Expense:

    def __init__(self, expense_id, trip_id, category, amount, description):
        self.expense_id = expense_id
        self.trip_id = trip_id
        self.category = category
        self.amount = float(amount)
        self.description = description

    def display_expense(self):
        print("\n----- EXPENSE DETAILS -----")
        print("Expense ID:", self.expense_id)
        print("Trip ID:", self.trip_id)
        print("Category:", self.category)
        print("Amount:", self.amount)
        print("Description:", self.description)