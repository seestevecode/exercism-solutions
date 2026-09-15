"""Determine which items a person is allergic to, given a score"""

# pylint: disable=missing-function-docstring

ALLERGIES = {
    'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8,
    'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128
}

class Allergies:  # pylint: disable=missing-class-docstring

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return (self.score & ALLERGIES[item]) > 0

    @property
    def lst(self):
        return [allergen for allergen in ALLERGIES if Allergies.allergic_to(self, allergen)]
