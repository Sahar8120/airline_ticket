from view.console_window import ConsoleWindow


class PassengerView:
    def __init__(self):
        self.window = ConsoleWindow(title="PASSENGER DETAILS")

    def get_passenger_details(self):
        self.window.render("Please enter your details:")

        name = self.window.get_input("Enter name: ")
        family = self.window.get_input("Enter family: ")
        phone = self.window.get_input("Enter phone number (e.g. 09123456789): ")
        national_id = self.window.get_input("Enter national ID (10 digits): ")

        return name, family, phone, national_id