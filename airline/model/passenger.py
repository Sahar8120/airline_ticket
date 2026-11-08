from tools.validation import name_validator, family_validator, national_id_validator, phone_validator

class Passenger:
    def __init__(self, name, family, phone_number, national_id):

        self.name = name
        self.family = family
        self.phone_number = phone_number
        self.national_id = national_id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name_validator(name)
        self.__name = name


    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family):
        family_validator(family)
        self.__family = family


    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        phone_validator(phone_number)
        self.__phone_number = phone_number

    
    @property
    def national_id(self):
        return self.__national_id

    @national_id.setter
    def national_id(self, national_id):
        national_id_validator(national_id)
        self.__national_id = national_id

    def get_info(self):
        return {
            "name": self.name,
            "family": self.family,
            "phone_number": self.phone_number,
            "national_id": self.national_id
        }

    def __repr__(self):
        return f"[Passenger: {self.name} {self.family}, National ID: {self.national_id}]"