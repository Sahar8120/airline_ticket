from utils.decorators import ejra_konande

class TicketBL:
    def __init__(self, ticket_da):
        self.ticket_da = ticket_da

    @ejra_konande
    def cancel_ticket(self, ticket_number):
        ticket = self.ticket_da.get_by_number(ticket_number)
        if not ticket:
            raise ValueError("Ticket not found!")

        if ticket.status == "Cancelled":
            raise ValueError("Ticket is already cancelled!")

        ticket.cancel()
        self.ticket_da.update_status(ticket_number, "Cancelled")

        return f"Ticket {ticket_number} cancelled successfully."

    @ejra_konande
    def get_passenger_tickets(self, national_id):
        tickets = self.ticket_da.get_by_passenger_id(national_id)
        if not tickets:
            raise ValueError("No tickets found for this passenger.")
        return tickets

    @ejra_konande
    def get_flight_tickets(self, flight_number):
        return self.ticket_da.get_by_flight_number(flight_number)