from datetime import datetime
from trip import Trip
from expense import Expense
from trip_manager import TripManager
from expense_manager import ExpenseManager


trip_manager = TripManager()
expense_manager = ExpenseManager()


def add_trip():

    trip_id = input("Enter Trip ID: ")
    destination = input("Enter Destination: ")

    # Date validation
    try:
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        if start > end:
            print("Start date cannot be after end date!")
            return

    except ValueError:
        print("Invalid date! Use YYYY-MM-DD format.")
        return

    # Budget validation
    try:
        budget = float(input("Enter Budget: "))

        if budget <= 0:
            print("Budget must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid numeric budget!")
        return

    trip = Trip(
        trip_id,
        destination,
        start_date,
        end_date,
        budget
    )

    trip_manager.add_trip(trip)





def view_trips():
    print("View Trips function is called!")
    trip_manager.view_trips()



def add_expense():

    expense_id = input("Enter Expense ID: ")
    trip_id = input("Enter Trip ID: ")

    trip = trip_manager.search_trip(trip_id)

    if trip is None:
        print("Trip not found!")
        return

    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: "))

        if amount <= 0:
            print("Expense amount must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid numeric amount!")
        return

    description = input("Enter Description: ")

    expense = Expense(
        expense_id,
        trip_id,
        category,
        amount,
        description
    )

    expense_manager.add_expense(expense)


def view_expenses():

    expense_manager.view_expenses()


def view_total_expenses():

    total = expense_manager.total_expenses()

    print("Total Expenses:", total)


def check_budget():

    trip_id = input("Enter Trip ID: ")

    trip = trip_manager.search_trip(trip_id)

    if trip is None:
        print("Trip not found!")
        return

    total = expense_manager.trip_total_expenses(trip_id)

    remaining = trip.budget - total

    print("Trip Budget:", trip.budget)
    print("Total Expenses:", total)
    print("Remaining Budget:", remaining)
def update_expense():
    expense_id = input("Enter Expense ID to update: ")
    expense_manager.update_expense(expense_id)


def delete_expense():
    expense_id = input("Enter Expense ID to delete: ")
    expense_manager.delete_expense(expense_id)

def generate_trip_report():
    trip_id = input("Enter Trip ID: ")
    trip_manager.generate_trip_report(trip_id, expense_manager)
def main():

    while True:

        print("\n========== TRAVELMATE ==========")

        print("1. Add New Trip")
        print("2. View All Trips")
        print("3. Add Expense")
        print("4. View All Expenses")
        print("5. View Total Expenses")
        print("6. Check Remaining Budget")
        print("7. Exit")
        print("8. Update Trip")
        print("9. Delete Trip")
        print("10. Update Expense")
        print("11. Delete Expense")
        print("12. Generate Trip Expense Report")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_trip()

        elif choice == "2":
            view_trips()

        elif choice == "3":
            add_expense()

        elif choice == "4":
            view_expenses()

        elif choice == "5":
            view_total_expenses()

        elif choice == "6":
            check_budget()

        elif choice == "7":
            print("Thank you for using TravelMate!")
            break
        elif choice == "8":
            trip_id = input("Enter Trip ID: ")
            trip_manager.update_trip(trip_id)

        elif choice == "9":
            trip_id = input("Enter Trip ID: ")
            trip_manager.delete_trip(trip_id)
        elif choice == "10":
             update_expense()

        elif choice == "11":
             delete_expense()
        elif choice == "12":
            generate_trip_report()
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
