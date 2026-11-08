from datetime import datetime

class Payment:
    def __init__(self, payment_id, ticket, payment_method):
        self.payment_id = payment_id
        self.ticket = ticket
        self.amount = ticket.price
        self.payment_method = payment_method
        self.status = "Pending"
        self.payment_date = None

    def process_payment(self) -> bool:

        if self.ticket.status != "Reserved":
            self.status = "Failed"
            return False


        if self.status != "Pending":
            return False


        if self.payment_method not in ["Cash", "Card", "Online"] or self.amount <= 0:
            self.status = "Failed"
            return False


        self.status = "Paid"
        self.payment_date = datetime.now()
        self.ticket.status = "Paid"
        return True

    def refund_payment(self) -> bool:
        if self.status != "Paid":
            return False

        self.status = "Refunded"
        self.ticket.status = "Cancelled"
        return True

    def get_details(self):
        return (
            f"Payment ID: {self.payment_id} | "
            f"Ticket: {self.ticket.ticket_number} | "
            f"Amount: ${self.amount} | "
            f"Method: {self.payment_method} | "
            f"Status: {self.status}"
        )