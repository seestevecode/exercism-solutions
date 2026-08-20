"""Estimate of integer square root"""

def square_root(number):
    counter = 0
    while (counter + 1) * (counter + 1) <= number:
        counter += 1

    return counter
