class FlightDA:
    def __init__(self):
        self.flights = []

    def save(self, flight):
        self.flights.append(flight)

    def get_all(self):
        return self.flights