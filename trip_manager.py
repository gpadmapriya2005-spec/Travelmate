
from csv_manager import CSVManager


class TripManager:

    def __init__(self):
        self.trips = CSVManager.load_trips()

    # 1. Add a new trip with duplicate ID validation
    def add_trip(self, trip):

        # Reload trips from CSV
        self.trips = CSVManager.load_trips()

        new_id = str(trip.trip_id).strip()

        # Check duplicate ID
        for existing_trip in self.trips:

            existing_id = str(existing_trip.trip_id).strip()

            if new_id == existing_id:
                print("Error: Trip ID already exists!")
                return

        # Add trip if ID is unique
        self.trips.append(trip)

        CSVManager.save_trips(self.trips)

        print("Trip added successfully!")

    # 2. View all trips
    def view_trips(self):

        self.trips = CSVManager.load_trips()

        print("\n========== ALL TRIPS ==========")

        if not self.trips:
            print("No trips available!")
            return

        print("Total trips:", len(self.trips))

        for trip in self.trips:
            trip.display_trip()

    # 3. Search trip using ID
    def search_trip(self, trip_id):

        for trip in self.trips:

            if str(trip.trip_id).strip() == str(trip_id).strip():
                return trip

        return None

    # 4. Update trip
    def update_trip(self, trip_id):

        self.trips = CSVManager.load_trips()

        trip = self.search_trip(trip_id)

        if trip is None:
            print("Trip not found!")
            return

        print("\nEnter New Trip Details")

        destination = input("Enter Destination: ")
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")

        try:
            budget = float(input("Enter Budget: "))

            if budget <= 0:
                print("Budget must be greater than zero!")
                return

        except ValueError:
            print("Please enter a valid budget!")
            return

        trip.destination = destination
        trip.start_date = start_date
        trip.end_date = end_date
        trip.budget = budget

        CSVManager.save_trips(self.trips)

        print("Trip updated successfully!")

    # 5. Delete trip
    def delete_trip(self, trip_id):

        self.trips = CSVManager.load_trips()

        trip = self.search_trip(trip_id)

        if trip is None:
            print("Trip not found!")
            return

        self.trips.remove(trip)

        CSVManager.save_trips(self.trips)

        print("Trip deleted successfully!")

    # 6. Check duplicate Trip IDs
    def check_duplicate_ids(self):

        ids = set()
        duplicates = set()

        for trip in self.trips:

            trip_id = str(trip.trip_id).strip()

            if trip_id in ids:
                duplicates.add(trip_id)

            ids.add(trip_id)

        if duplicates:
            print("Duplicate Trip IDs found:", duplicates)
        else:
            print("No duplicate Trip IDs found!")
    
    # Generate Trip-wise Expense Report
    def generate_trip_report(self, trip_id, expense_manager):

        self.trips = CSVManager.load_trips()

        trip = self.search_trip(trip_id)

        if trip is None:
            print("Trip not found!")
            return

        total_expenses = expense_manager.trip_total_expenses(trip_id)
        remaining_budget = trip.budget - total_expenses

        print("\n========== TRIP EXPENSE REPORT ==========")
        print("Trip ID:", trip.trip_id)
        print("Destination:", trip.destination)
        print("Start Date:", trip.start_date)
        print("End Date:", trip.end_date)
        print("----------------------------------------")
        print("Total Budget: ₹", trip.budget)
        print("Total Expenses: ₹", total_expenses)
        print("Remaining Budget: ₹", remaining_budget)
        print("----------------------------------------")

        if remaining_budget >= 0:
            print("Budget Status: Within Budget")
        else:
            print("Budget Status: Budget Exceeded")

        print("========================================")
