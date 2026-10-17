class TicketDA:
    def __init__(self):
        self.tickets = []

    def save(self, ticket):
        self.tickets.append(ticket)

    def get_by_number(self, ticket_number):
        for t in self.tickets:
            if t.ticket_number == ticket_number:
                return t
        return None

    def get_all(self):
        return self.tickets