class TicketDA:
    def __init__(self):
        self.tickets = []

    def save(self, ticket):

        if not self.get_by_number(ticket.ticket_number):
            self.tickets.append(ticket)
            return True
        return False

    def get_all(self):
        return self.tickets

    def get_by_number(self, ticket_number):
        for t in self.tickets:
            if t.ticket_number == ticket_number:
                return t
        return None


    def get_by_passenger_id(self, national_id):
        return [t for t in self.tickets if t.passenger.national_id == national_id]


    def get_by_flight_number(self, flight_number):
        return [t for t in self.tickets if t.flight.flight_number == flight_number]


    def update_status(self, ticket_number, new_status):
        ticket = self.get_by_number(ticket_number)
        if ticket:
            ticket.status = new_status
            return True
        return False