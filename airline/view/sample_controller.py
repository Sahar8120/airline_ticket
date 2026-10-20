from utils.decorators import ejra_konande
from utils.logger import Logger


class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class SampleController:
    def __init__(self):


        pass

    @ejra_konande
    def save(self, a, b):

        sample = Sample(a, b)
        return True, f"Info : {sample} Saved"

    @ejra_konande
    def update(self, a, b):
        return True, f"Updated {a} with {b}"

    @ejra_konande
    def delete(self, a):
        return True, f"Deleted item {a}"

    @ejra_konande
    def find_by_id(self, a):
        return True, f"Found item with ID {a}"