from model.ticket import Ticket
from model.payment import Payment
from data_access.ticket_da import TicketDA
from business_logic.passenger_bl import PassengerBL


class BookingService:
    def __init__(self):
        self.ticket_da = TicketDA()
        self.passenger_bl = PassengerBL()

    def book_ticket(self, name, family, phone, nid, flight, seat, method, t_counter, p_counter):

        success, passenger = self.passenger_bl.register_passenger(name, family, phone, nid)

        if not success:
            raise ValueError(f"Passenger Error: {passenger}")


        if not flight.reserve_seat(seat):
            raise ValueError("Seat is already taken!")


        ticket = Ticket(f"TK-{t_counter}", passenger, flight, seat, flight.price)


        payment = Payment(p_counter, ticket, method)

        if not payment.process_payment():
            flight.cancel_seat(seat)
            raise ValueError("Payment failed!")

        self.ticket_da.save(ticket)

        return f"Booked successfully. Ticket: {ticket.ticket_number}"