from view.main_view import MainView
from view.passenger_view import PassengerView
from view.flight_view import FlightView
from view.ticket_view import TicketView
from model.passenger import Passenger
from model.flight import Flight

from data_access.flight_da import FlightDA
from data_access.ticket_da import TicketDA
from data_access.passenger_da import PassengerDA
from business_logic.booking_bl import BookingBL


class MainController:
    def __init__(self):
        self.main_view = MainView()
        self.passenger_view = PassengerView()
        self.flight_view = FlightView()
        self.ticket_view = TicketView()


        self.flight_da = FlightDA()
        self.ticket_da = TicketDA()
        self.passenger_da = PassengerDA()


        self.booking_bl = BookingBL(self.ticket_da, self.passenger_da)

        self.ticket_counter = 1000
        self.payment_counter = 5000
        self._load_initial_data()

    def _load_initial_data(self):
        try:
            f1 = Flight("IR-123", "Mahan", "Tehran", "Istanbul", "10:00", "12:00", 500.0)
            f2 = Flight("EK-456", "Emirates", "Tehran", "Dubai", "14:00", "16:00", 300.0)
            self.flight_da.save(f1)
            self.flight_da.save(f2)
        except Exception as e:
            print(f"Error loading flights: {e}")

    def run(self):
        while True:
            choice = self.main_view.show_main_menu()

            if choice == "1":
                flights = self.flight_da.get_all()
                self.flight_view.show_flights(flights)

            elif choice == "2":
                name, family, phone, national_id = self.passenger_view.get_passenger_details()
                try:
                    passenger = Passenger(name, family, phone, national_id)
                except ValueError as e:
                    self.main_view.show_message(f"Validation Error: {e}")
                    continue

                flights = self.flight_da.get_all()
                selected_flight = self.flight_view.get_flight_choice(flights)
                if not selected_flight: continue

                seat_number = self.flight_view.get_seat_choice(selected_flight.get_available_seats())
                method = self.ticket_view.get_payment_method()

                try:
                    self.ticket_counter += 1
                    self.payment_counter += 1

                   
                    ticket = self.booking_bl.book_ticket(
                        passenger, selected_flight, seat_number,
                        method, self.ticket_counter, self.payment_counter
                    )

                    self.main_view.show_message("Success! Ticket Booked & Paid.")
                    self.ticket_view.show_ticket_details(ticket)
                except ValueError as e:
                    self.main_view.show_message(f"Error: {e}")

            elif choice == "3":
                ticket_num = self.ticket_view.get_ticket_number_to_cancel()
                try:
                    self.booking_bl.cancel_ticket(ticket_num)
                    self.main_view.show_message(f"Ticket {ticket_num} cancelled successfully.")
                except ValueError as e:
                    self.main_view.show_message(f"Error: {e}")

            elif choice == "4":
                self.main_view.show_message("Goodbye!")
                break
            else:
                self.main_view.show_message("Invalid choice!")