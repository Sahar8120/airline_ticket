class TicketView:
    def get_payment_method(self):
        print("\n--- Payment ---")
        print("Available methods: Cash, Card, Online")
        return input("Enter payment method: ")

    def show_ticket_details(self, ticket):
        print("\n--- Ticket Details ---")
        print(ticket.get_details())

    def get_ticket_number_to_cancel(self):
        return input("\nEnter your Ticket Number to cancel: ")