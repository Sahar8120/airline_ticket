import unittest
from model.passenger import Passenger
from model.flight import Flight
from model.ticket import Ticket
from model.payment import Payment

class TestBookingAndPayment(unittest.TestCase):

    def setUp(self):

        self.passenger = Passenger("Ali", "Rezaei", "09123456789", "1234567890")
        self.flight = Flight("IR-123", "Mahan", "Tehran", "Istanbul", "10:00", "12:00", 500.0)
        self.flight.reserve_seat("1A")
        self.ticket = Ticket("TK-1001", self.passenger, self.flight, "1A")

    def test_ticket_price_and_status(self):
        self.assertEqual(self.ticket.price, 500.0)
        self.assertEqual(self.ticket.status, "Reserved")

    def test_cancel_ticket_frees_seat(self):
        self.ticket.cancel()
        self.assertEqual(self.ticket.status, "Cancelled")
        self.assertIn("1A", self.flight.get_available_seats())

    def test_payment_success(self):
        pay = Payment(5000, self.ticket, "Online")
        self.assertTrue(pay.process_payment())
        self.assertEqual(pay.status, "Paid")
        self.assertEqual(self.ticket.status, "Paid")

    def test_invalid_payment_method_raises_error(self):
        with self.assertRaises(ValueError):
            Payment(5000, self.ticket, "Bitcoin")

    def test_refund_payment(self):
        pay = Payment(5000, self.ticket, "Card")
        pay.process_payment()
        self.assertTrue(pay.refund_payment())
        self.assertEqual(pay.status, "Refunded")
        self.assertEqual(self.ticket.status, "Cancelled")

if __name__ == '__main__':
    unittest.main()