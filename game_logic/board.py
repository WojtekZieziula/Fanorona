from exceptions.exceptions import InvalidArgumentException


class Board:
    def __init__(self, rows, columns):
        self.set_shape(rows, columns)

    def set_shape(self, rows, columns):
        if rows <= 0 or columns <= 0:
            raise InvalidArgumentException("rows/columns amount has to be a positive number!")
        self.rows = rows
        self.columns = columns

    def get_shape(self):
        return self.rows, self.columns

#       0   1   2   3   4
# 0     X - X - X - X - X
#       | \ | / | \ | / |
# 1     X - X - X - X - X
#       | / | \ | / | \ |
# 2     X - X - X - X - X

# (0, 0): [(0, 1), (1, 0), (1, 1)]
# (0, 1): [(0, 0), (1, 1), (0, 2)]
# (0, 2): []