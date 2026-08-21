"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    return (
        EQUAL if list_one == list_two else
        SUBLIST if is_sublist(list_one, list_two) else
        SUPERLIST if is_sublist(list_two, list_one) else
        UNEQUAL
    )


def is_sublist(list_one, list_two):
    if not list_one:
        return True

    length_one, length_two = len(list_one), len(list_two)
    chunked_two = [list_two[index:index+length_one] for index in range(length_two - length_one + 1)]
    return list_one in chunked_two
