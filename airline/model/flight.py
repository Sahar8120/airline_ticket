class Flight:
    def __init__(self, flight_number, airline, origin, destination, start_data_time, end_data_time, price):
        self.flight_number = flight_number
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.start_time = start_data_time
        self.end_time = end_data_time
        self.price = price

        self.seats = {f"{i}A": False for i in range(1, 11)}

    def get_available_seats(self):
        return [seat for seat, is_reserved in self.seats.items() if not is_reserved]

    def reserve_seat(self, seat_number):
        if seat_number in self.seats and not self.seats[seat_number]:
            self.seats[seat_number] = True
            return True
        return False

    def cancel_seat(self, seat_number):
        if seat_number in self.seats:
            self.seats[seat_number] = False

    def get_details(self):
        return f"Flight {self.flight_number} ({self.airline}) | {self.origin} -> {self.destination} | Price: {self.price}"