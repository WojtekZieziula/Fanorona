from exceptions.exceptions import InvalidArgumentException


class Board:
    def __init__(self, rows, columns):
        self.set_shape(rows, columns)

    def set_shape(self, rows, columns):
        if rows <= 0 or columns <= 0:
            raise InvalidArgumentException("rows/columns amount has to be a positive number!")
        self.rows = rows
        self.columns = columns
