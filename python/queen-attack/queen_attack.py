"""Indicate whether two Queens on a chess board can attack each other"""

# pylint: disable=missing-function-docstring

class Queen:  # pylint: disable=missing-class-docstring,too-few-public-methods
    def __init__(self, row, column):
        if row < 0:
            raise ValueError('row not positive')
        if row > 7:
            raise ValueError('row not on board')
        if column < 0:
            raise ValueError('column not positive')
        if column > 7:
            raise ValueError('column not on board')

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if (self.row, self.column) == (another_queen.row, another_queen.column):
            raise ValueError('Invalid queen position: both queens in the same square')
            
        return (
            self.column == another_queen.column
            or self.row == another_queen.row
            or abs(self.column - another_queen.column) 
                == abs(self.row - another_queen.row)
        )        
