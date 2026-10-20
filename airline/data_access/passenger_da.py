class PassengerDA:
    def __init__(self):
        self.passengers = []

    def save(self, passenger):
        if not self.get_by_national_id(passenger.national_id):
            self.passengers.append(passenger)
            return True
        return False

    def get_all(self):
        return self.passengers

    def get_by_national_id(self, nid):
        for p in self.passengers:
            if p.national_id == nid:
                return p
        return None

    def search_by_name(self, name, family):
        results = []
        for p in self.passengers:
            if name.lower() in p.name.lower() and family.lower() in p.family.lower():
                results.append(p)
        return results

    def update_passenger(self, nid, new_name=None, new_family=None, new_phone=None):
        passenger = self.get_by_national_id(nid)
        if passenger:
            if new_name: passenger.name = new_name
            if new_family: passenger.family = new_family
            if new_phone: passenger.phone_number = new_phone
            return True
        return False