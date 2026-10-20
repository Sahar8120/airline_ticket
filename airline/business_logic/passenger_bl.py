from model.passenger import Passenger
from data_access.passenger_da import PassengerDA
from utils.logger import Logger
from utils.decorators import ejra_konande


class PassengerBL:
    def __init__(self):

        self.passenger_da = PassengerDA()

    @ejra_konande
    def register_passenger(self, name, family, phone, nid):
        """
        ثبت‌نام مسافر جدید.
        اگر مسافر قبلاً با همین کد ملی ثبت شده باشد، همان مسافر قبلی برگردانده می‌شود.
        """

        existing_passenger = self.passenger_da.get_by_national_id(nid)

        if existing_passenger:
            Logger.info(f"Passenger with National ID {nid} already exists in system.")
            return existing_passenger


        new_passenger = Passenger(name, family, phone, nid)
        self.passenger_da.save(new_passenger)

        return new_passenger

    @ejra_konande
    def get_passenger(self, nid):
        """
        دریافت اطلاعات یک مسافر بر اساس کد ملی
        """
        passenger = self.passenger_da.get_by_national_id(nid)
        if not passenger:
            raise ValueError(f"No passenger found with National ID: {nid}")
        return passenger

    @ejra_konande
    def get_all_passengers(self):
        """
        دریافت لیست تمام مسافران
        """
        return self.passenger_da.get_all()