"""Calculate score of Yacht dice for a given category"""

# pylint: disable=missing-function-docstring

from collections import Counter

ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
YACHT = 11
CHOICE = 12

def minor_scores(dice, target):
    return target * dice.count(target)


def full_house(dice):
    return sum(dice) if sorted(Counter(dice).values()) == [2, 3] else 0


def four_of_a_kind(dice):
    counts = Counter(dice)
    return next((die * 4 for die, count in counts.items() if count >= 4), 0)     


def little_straight(dice):
    return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0


def big_straight(dice):
    return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0


def yacht(dice):
    return 50 if len(set(dice)) == 1 else 0

    
def score(dice, category):
    if ONES <= category <= SIXES:
        return minor_scores(dice, category)

    major_scorers = {
        FULL_HOUSE: full_house,
        FOUR_OF_A_KIND: four_of_a_kind,
        LITTLE_STRAIGHT: little_straight,
        BIG_STRAIGHT: big_straight,
        YACHT: yacht,
        CHOICE: sum
    }

    return major_scorers[category](dice)
