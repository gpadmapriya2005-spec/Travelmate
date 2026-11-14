class Trip:

    def __init__(self, trip_id, destination, start_date, end_date, budget):
        self.trip_id = trip_id
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.budget = float(budget)

    def display_trip(self):
        print("\n----- TRIP DETAILS -----")
        print("Trip ID:", self.trip_id)
        print("Destination:", self.destination)
        print("Start Date:", self.start_date)
        print("End Date:", self.end_date)
        print("Budget:", self.budget)