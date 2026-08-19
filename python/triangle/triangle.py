"""Functions to determine the type of a triangle"""

def equilateral(sides):
    return valid(sides) and len(set(sides)) == 1


def isosceles(sides):
    return valid(sides) and len(set(sides)) <= 2


def scalene(sides):
    return valid(sides) and len(set(sides)) == 3


def valid(sides):
    a, b, c = sides
    return (
        a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a
    )
    