class FlightView:
    def show_flights(self, flights):
        print("\n--- Available Flights ---")
        for i, f in enumerate(flights):
            print(f"{i+1}. {f.get_details()}")
            print(f"   Available Seats: {f.get_available_seats()}")

    def get_flight_choice(self, flights):
        try:
            choice = int(input("\nSelect flight number (e.g. 1): ")) - 1
            if 0 <= choice < len(flights):
                return flights[choice]
            return None
        except ValueError:
            return None

    def get_seat_choice(self, available_seats):
        return input("Choose a seat number from the list above (e.g., 1A): ")