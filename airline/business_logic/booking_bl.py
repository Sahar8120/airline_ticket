from model.ticket import Ticket
from model.payment import Payment

class BookingBL:
    def __init__(self, ticket_da, passenger_da): # <-- passenger_da اضافه شد
        self.ticket_da = ticket_da
        self.passenger_da = passenger_da

    def book_ticket(self, passenger, flight, seat_number, payment_method, ticket_counter, payment_counter):

        self.passenger_da.save(passenger)


        if not flight.reserve_seat(seat_number):
            raise ValueError("Seat is already taken!")


        ticket_number = f"TK-{ticket_counter}"
        ticket = Ticket(ticket_number, passenger, flight, seat_number)


        payment = Payment(payment_counter, ticket, payment_method)
        if not payment.process_payment():
            flight.cancel_seat(seat_number)
            raise ValueError("Payment failed!")


        self.ticket_da.save(ticket)
        return ticket

    def cancel_ticket(self, ticket_number):
        ticket = self.ticket_da.get_by_number(ticket_number)
        if not ticket:
            raise ValueError("Ticket not found!")
        ticket.cancel()
        return ticket