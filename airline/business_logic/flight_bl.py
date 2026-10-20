from utils.decorators import ejra_konande


class FlightBL:
    def __init__(self, flight_da):
        self.flight_da = flight_da

    @ejra_konande
    def get_all_flights(self):
        return self.flight_da.get_all()

    @ejra_konande
    def search_flights(self, origin, destination):
        return self.flight_da.search_flights(origin, destination)

    @ejra_konande
    def edit_flight_info(self, flight_number, new_airline, new_origin, new_destination, new_price):

        flight = self.flight_da.get_by_number(flight_number)
        if not flight:
            raise ValueError(f"Flight {flight_number} not found!")

        success = self.flight_da.update_flight(flight_number, new_airline, new_origin, new_destination, new_price)
        if success:
            return f"Flight {flight_number} updated successfully."
        return "Update failed."