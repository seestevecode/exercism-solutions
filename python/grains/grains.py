"""Functions to calculate the number of grains of wheat on a chessboard"""

def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    return 2 ** (number - 1)


def total():
    return sum(square(num) for num in range(1, 65))
