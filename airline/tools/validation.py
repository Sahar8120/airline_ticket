import re
from datetime import date

# ==========================================
# Public Validators
# ==========================================

def date_validator(date_):
    if not isinstance(date_, date):
        raise ValueError("Invalid Date")

# ==========================================
# Passenger Validators
# ==========================================

def name_validator(name):

    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid Name! (Only letters, 3-30 chars)")

def family_validator(family):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", family):
        raise ValueError("Invalid Family! (Only letters, 3-30 chars)")

def national_id_validator(national_id):

    if not re.match(r"^\d{10}$", national_id):
        raise ValueError("Invalid National ID! (Must be exactly 10 digits)")

def phone_validator(phone_number):

    if not re.match(r"(09|\+98)\d{9}", phone_number):
        raise ValueError("Invalid Phone Number! (e.g., 09123456789)")