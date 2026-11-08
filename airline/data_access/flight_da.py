class FlightDA:
    def __init__(self):
        self.flights = []

    def save(self, flight):

        if not self.get_by_number(flight.flight_number):
            self.flights.append(flight)
            return True
        return False

    def get_all(self):
        return self.flights

    def get_by_number(self, flight_number):
        for f in self.flights:
            if f.flight_number == flight_number:
                return f
        return None


    def search_flights(self, origin=None, destination=None):
        results = self.flights
        if origin:
            results = [f for f in results if origin.lower() in f.origin.lower()]
        if destination:
            results = [f for f in results if destination.lower() in f.destination.lower()]
        return results


    def update_flight(self, flight_number, new_airline=None, new_origin=None, new_destination=None, new_price=None):
        flight = self.get_by_number(flight_number)
        if flight:
            if new_airline:
                flight.airline = new_airline
            if new_origin:
                flight.origin = new_origin
            if new_destination:
                flight.destination = new_destination
            if new_price:
                flight.price = new_price
            return True
        return False