class Ticket:
    def __init__(self, ticket_number, passenger, flight, seat_number, price):
        self.ticket_number = ticket_number
        self.passenger = passenger
        self.flight = flight
        self.seat_number = seat_number
        self.price = price
        self.status = "Reserved"
        self.payment_date = None

    def process(self):

        self.status = "Paid"
        self.payment_date = "2026-10-25"
        return True

    def cancel(self):
        self.status = "Cancelled"
        self.flight.cancel_seat(self.seat_number)

    def get_details(self):
        return f"Ticket {self.ticket_number} | Passenger: {self.passenger.name} {self.passenger.family} | Flight: {self.flight.flight_number} | Seat: {self.seat_number} | Price: {self.price} | Status: {self.status}"