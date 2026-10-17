from model.passenger import Passenger
from model.flight import Flight
from model.ticket import Ticket
from model.payment import Payment

from view.main_view import MainView
from view.passenger_view import PassengerView
from view.flight_view import FlightView
from view.ticket_view import TicketView


def main():

    main_view = MainView()
    passenger_view = PassengerView()
    flight_view = FlightView()
    ticket_view = TicketView()


    try:
        flight1 = Flight("IR-123", "Mahan", "Tehran", "Istanbul", "10:00", "12:00", 500.0)
        flight2 = Flight("EK-456", "Emirates", "Tehran", "Dubai", "14:00", "16:00", 300.0)
        flights = [flight1, flight2]
    except ValueError as e:
        print(f"Error creating initial flights: {e}")
        return

    tickets = []
    payments = []
    ticket_counter = 1000
    payment_counter = 5000

    while True:
        choice = main_view.show_main_menu()


        if choice == "1":
            flight_view.show_flights(flights)


        elif choice == "2":
            name, family, phone, national_id = passenger_view.get_passenger_details()


            try:
                passenger = Passenger(name, family, phone, national_id)
            except ValueError as e:
                main_view.show_message(f"Validation Error: {e}")
                continue


            selected_flight = flight_view.get_flight_choice(flights)
            if not selected_flight:
                main_view.show_message("Error: Invalid flight selection.")
                continue


            seat_number = flight_view.get_seat_choice(selected_flight.get_available_seats())


            if selected_flight.reserve_seat(seat_number):
                ticket_counter += 1
                new_ticket = Ticket(f"TK-{ticket_counter}", passenger, selected_flight, seat_number)


                method = ticket_view.get_payment_method()
                payment_counter += 1

                try:

                    payment = Payment(payment_counter, new_ticket, method)

                    if payment.process_payment():
                        tickets.append(new_ticket)
                        payments.append(payment)
                        main_view.show_message("Success! Ticket Booked & Paid.")
                        ticket_view.show_ticket_details(new_ticket)
                    else:
                        selected_flight.cancel_seat(seat_number)
                        main_view.show_message("Payment Failed! Seat released.")

                except ValueError as e:

                    main_view.show_message(f"Payment Error: {e}")
                    selected_flight.cancel_seat(seat_number)
            else:
                main_view.show_message("Error: Seat is already taken or invalid!")


        elif choice == "3":
            ticket_num = ticket_view.get_ticket_number_to_cancel()
            found = False
            for t in tickets:
                if t.ticket_number == ticket_num:
                    t.cancel()
                    main_view.show_message(f"Ticket {ticket_num} cancelled successfully.")
                    found = True
                    break
            if not found:
                main_view.show_message("Error: Ticket not found!")


        elif choice == "4":
            main_view.show_message("Goodbye! Have a nice flight.")
            break

        else:
            main_view.show_message("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()