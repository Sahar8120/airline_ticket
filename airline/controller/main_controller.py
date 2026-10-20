from view.main_view import MainView
from view.passenger_view import PassengerView
from view.flight_view import FlightView
from view.ticket_view import TicketView

from model.passenger import Passenger
from data_access.flight_da import FlightDA
from data_access.passenger_da import PassengerDA
from data_access.ticket_da import TicketDA

from business_logic.booking_bl import BookingBL
from business_logic.flight_bl import FlightBL
from business_logic.ticket_bl import TicketBL

from utils.validation import Validator, ValidationError


class MainController:
    def __init__(self):
        self.main_view = MainView()
        self.passenger_view = PassengerView()
        self.flight_view = FlightView()
        self.ticket_view = TicketView()

        self.flight_da = FlightDA()
        self.passenger_da = PassengerDA()
        self.ticket_da = TicketDA()

        self.booking_bl = BookingBL(self.ticket_da, self.passenger_da)
        self.flight_bl = FlightBL(self.flight_da)
        self.ticket_bl = TicketBL(self.ticket_da)

        self.ticket_counter = 1000
        self.payment_counter = 5000

    def run(self):
        while True:
            
            choice = self.main_view.show_main_menu()

            if choice == "1":
                flights = self.flight_bl.get_all_flights()
                self.flight_view.show_flights(flights)

            elif choice == "2":
                f_num, airline, origin, dest, price = self.flight_view.get_new_flight_details()
                try:
                    Validator.validate_positive_number(price, "Price")
                    self.flight_bl.add_flight(f_num, airline, origin, dest, price)
                    self.main_view.show_info(f"Flight {f_num} added successfully.")
                except (ValueError, ValidationError) as e:
                    self.main_view.show_error(str(e))

            elif choice == "3":
                name, family, phone, nid = self.passenger_view.get_passenger_details()
                try:
                    Validator.validate_name(name)
                    Validator.validate_name(family, "Family")
                    Validator.validate_phone(phone)
                    Validator.validate_national_id(nid)
                except ValidationError as e:
                    self.main_view.show_error(str(e))
                    continue

                flights = self.flight_bl.get_all_flights()
                if not flights:
                    self.main_view.show_error("No flights available! Add a flight first.")
                    continue

                passenger = Passenger(name, family, phone, nid)


                selected_flight = self.flight_view.get_flight_choice(flights)
                if not selected_flight:
                    continue


                seat = self.flight_view.get_seat_choice(selected_flight.get_available_seats())
                if not seat:
                    continue


                method = self.ticket_view.get_payment_method()

                self.ticket_counter += 1
                self.payment_counter += 1

                try:
                    self.booking_bl.book_ticket(
                        passenger, selected_flight, seat, method, self.ticket_counter, self.payment_counter
                    )
                    self.main_view.show_info(f"Success! Ticket No: TK-{self.ticket_counter}")
                except ValueError as e:
                    self.main_view.show_error(str(e))

            elif choice == "4":
                t_num = self.ticket_view.get_ticket_number_to_cancel()
                if t_num:
                    try:
                        self.ticket_bl.cancel_ticket(t_num)
                        self.main_view.show_info(f"Ticket {t_num} cancelled successfully.")
                    except ValueError as e:
                        self.main_view.show_error(str(e))

            elif choice == "5":
                self.main_view.show_info("Goodbye!")
                break

            else:
                if choice:
                    self.main_view.show_error("Invalid choice!")