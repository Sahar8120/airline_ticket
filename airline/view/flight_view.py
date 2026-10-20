from view.console_window import ConsoleWindow


class FlightView:
    def __init__(self):
        self.window = ConsoleWindow(title="FLIGHT SYSTEM")

    def show_flights(self, flights):
        if not flights:
            self.window.render("No flights available. Please add a flight first.", is_error=True)
            return

        output = "--- Available Flights ---\n"
        for i, f in enumerate(flights):
            output += f"{i + 1}. {f.get_details()}\n"

        self.window.render(output)

    def get_flight_choice(self, flights):
        while True:
            try:
                choice_str = self.window.get_input("Select flight number (0 to cancel): ")
                choice = int(choice_str)

                if choice == 0:
                    return None
                if 1 <= choice <= len(flights):
                    return flights[choice - 1]

                self.window.render("Invalid number. Please choose from the list.", is_error=True)
            except ValueError:
                self.window.render("Please enter a valid number!", is_error=True)

    def get_seat_choice(self, available_seats):
        if not available_seats:
            self.window.render("No seats available on this flight!", is_error=True)
            return None

        while True:
            seat = self.window.get_input(f"Choose a seat (Available: {', '.join(available_seats)}): ").upper()
            if seat in available_seats:
                return seat
            self.window.render("Seat is invalid or already taken. Try again.", is_error=True)

    def get_new_flight_details(self):
        self.window.render("--- Add New Flight ---")
        f_num = self.window.get_input("Flight Number (e.g. IR-123): ")
        airline = self.window.get_input("Airline: ")
        origin = self.window.get_input("Origin: ")
        dest = self.window.get_input("Destination: ")
        price_str = self.window.get_input("Price: ")


        try:
            price = float(price_str)
        except ValueError:
            price = 0.0

        return f_num, airline, origin, dest, price
