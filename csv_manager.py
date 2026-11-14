
import csv

from trip import Trip
from expense import Expense


class CSVManager:

    # Save trip records
    @staticmethod
    def save_trips(trips):

        with open("trips.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "trip_id",
                "destination",
                "start_date",
                "end_date",
                "budget"
            ])

            for trip in trips:
                writer.writerow([
                    trip.trip_id,
                    trip.destination,
                    trip.start_date,
                    trip.end_date,
                    trip.budget
                ])

        print("Trips saved successfully!")


    # Load trip records
    @staticmethod
    def load_trips():

        trips = []

        try:
            with open("trips.csv", "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    trip = Trip(
                        row["trip_id"],
                        row["destination"],
                        row["start_date"],
                        row["end_date"],
                        row["budget"]
                    )

                    trips.append(trip)

        except FileNotFoundError:
            print("Trip file not found!")

        return trips


    # Save expense records
    @staticmethod
    def save_expenses(expenses):

        with open("expenses.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "expense_id",
                "trip_id",
                "category",
                "amount",
                "description"
            ])

            for expense in expenses:
                writer.writerow([
                    expense.expense_id,
                    expense.trip_id,
                    expense.category,
                    expense.amount,
                    expense.description
                ])

        print("Expenses saved successfully!")


    # Load expense records
    @staticmethod
    def load_expenses():

        expenses = []

        try:
            with open("expenses.csv", "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    expense = Expense(
                        row["expense_id"],
                        row["trip_id"],
                        row["category"],
                        row["amount"],
                        row["description"]
                    )

                    expenses.append(expense)

        except FileNotFoundError:
            print("Expense file not found!")

        return expenses
