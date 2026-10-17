class PassengerView:
    def get_passenger_details(self):
        print("\n--- Passenger Details ---")
        name = input("Enter name: ")
        family = input("Enter family: ")
        phone = input("Enter phone number (11 digits): ")
        national_id = input("Enter national ID (10 digits): ")
        return name, family, phone, national_id