class PassengerDA:
    def __init__(self):

        self.passengers = []

    def save(self, passenger):

        existing = self.get_by_national_id(passenger.national_id)
        if not existing:
            self.passengers.append(passenger)

    def get_by_national_id(self, national_id):
        for p in self.passengers:
            if p.national_id == national_id:
                return p
        return None

    def get_all(self):
        return self.passengers