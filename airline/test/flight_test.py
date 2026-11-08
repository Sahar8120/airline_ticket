import unittest
from model.flight import Flight

class TestFlight(unittest.TestCase):

    def setUp(self):
        self.flight = Flight("IR-123", "Mahan", "Tehran", "Istanbul", "10:00", "12:00", 500.0)

    def test_valid_flight(self):
        self.assertEqual(self.flight.flight_number, "IR-123")
        self.assertEqual(self.flight.price, 500.0)

    def test_invalid_flight_number_raises_error(self):
        with self.assertRaises(ValueError):
            Flight("1234", "Mahan", "Tehran", "Istanbul", "10:00", "12:00", 500.0)

    def test_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            Flight("IR-123", "Mahan", "Tehran", "Istanbul", "10:00", "12:00", -100.0)

    def test_reserve_and_cancel_seat(self):
        self.assertTrue(self.flight.reserve_seat("1A"))
        self.assertFalse(self.flight.reserve_seat("1A"))
        self.flight.cancel_seat("1A")
        self.assertTrue(self.flight.reserve_seat("1A"))

if __name__ == '__main__':
    unittest.main()