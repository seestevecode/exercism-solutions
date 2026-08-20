"""Estimate of integer square root"""

def square_root(number):
    L = 0
    while (L + 1) * (L + 1) <= number:
        L += 1

    return L
