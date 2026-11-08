import unittest
from model.passenger import Passenger

class TestPassenger(unittest.TestCase):

    def test_valid_passenger(self):
        p = Passenger("Ali", "Sahar Maghooli", "09123456789", "1234567890")
        self.assertEqual(p.name, "Sahar")
        self.assertEqual(p.family, "Maghooli")

    def test_invalid_name_raises_error(self):
        with self.assertRaises(ValueError):
            Passenger("Sahar123", "Maghooli", "09123456789", "1234567890")
    def test_invalid_national_id_raises_error(self):
        with self.assertRaises(ValueError):
            Passenger("Sahar", "Maghooli", "09123456789", "12345")

    def test_invalid_phone_raises_error(self):
        with self.assertRaises(ValueError):
            Passenger("sahar", "Maghooli", "phone_number", "1234567890")

if __name__ == '__main__':
    unittest.main()