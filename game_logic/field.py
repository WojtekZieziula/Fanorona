from exceptions.exceptions import InvalidArgumentException

class Field:
    def __init__(self, value=""):
        self.set_value(value)

    def set_value(self, value):
        if value not in ["", "X", "O"]:
            raise InvalidArgumentException("Invalid field value!")
        self.value = value