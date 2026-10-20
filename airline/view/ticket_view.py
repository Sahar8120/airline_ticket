from view.console_window import ConsoleWindow

class TicketView:
    def __init__(self):
        self.window = ConsoleWindow(title="TICKET MENU")

    def get_payment_method(self):
        self.window.render("Available methods: Cash, Card, Online")
        return self.window.get_input("Enter payment method: ")

    def show_ticket_details(self, ticket):
        self.window.render(ticket.get_details())

    def get_ticket_number_to_cancel(self):
        return self.window.get_input("Enter your Ticket Number to cancel: ")