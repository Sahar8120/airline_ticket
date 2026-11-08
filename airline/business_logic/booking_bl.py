from model.ticket import Ticket
from model.payment import Payment
from utils.decorators import ejra_konande


class BookingBL:
    def __init__(self, ticket_da, passenger_da):
        self.ticket_da = ticket_da
        self.passenger_da = passenger_da

    @ejra_konande
    def book_ticket(self, passenger, flight, seat_number, payment_method, t_counter, p_counter):

        self.passenger_da.save(passenger)


        if not flight.reserve_seat(seat_number):
            raise ValueError("Seat is already taken!")


        ticket = Ticket(f"TK-{t_counter}", passenger, flight, seat_number, flight.price)
        payment = Payment(p_counter, ticket, payment_method)

        if not payment.process_payment():
            flight.cancel_seat(seat_number)
            raise ValueError("Payment failed!")


        self.ticket_da.save(ticket)
        return f"Success! Ticket No: {ticket.ticket_number}"