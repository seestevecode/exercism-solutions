"""Functions to determine the type of a triangle"""

def equilateral(sides):
    return valid(sides) and len(set(sides)) == 1


def isosceles(sides):
    return valid(sides) and len(set(sides)) <= 2


def scalene(sides):
    return valid(sides) and len(set(sides)) == 3


def valid(sides):
    side1, side2, side3 = sides
    return (
        side1 > 0 and side2 > 0 and side3 > 0 and 
        side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1
    )
    