import re
from datetime import datetime

class ValidationError(Exception):
    """کلاس اختصاصی برای خطاهای اعتبارسنجی"""
    pass

class Validator:
    @staticmethod
    def validate_name(name, field_name="Name"):
        if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
            raise ValidationError(f"{field_name} must be 3-30 characters and only letters!")

    @staticmethod
    def validate_national_id(nid):
        if not re.match(r"^\d{10}$", nid):
            raise ValidationError("National ID must be exactly 10 digits!")

    @staticmethod
    def validate_phone(phone):
        if not re.match(r"^(09|\+98)\d{9}$", phone):
            raise ValidationError("Phone must start with 09 or +98 and have 9 digits after!")

    @staticmethod
    def validate_positive_number(number, field_name="Number"):
        try:
            val = float(number)
            if val <= 0:
                raise ValidationError(f"{field_name} must be greater than zero!")
            return val
        except ValueError:
            raise ValidationError(f"{field_name} must be a valid number!")

    @staticmethod
    def validate_flight_number(f_num):
        if not re.match(r"^[A-Z]{2}-\d{3,4}$", f_num):
            raise ValidationError("Flight number format must be like 'IR-123' (2 letters, dash, 3-4 digits)!")

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValidationError("Date must be in YYYY-MM-DD format!")