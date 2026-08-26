"""Determine whether a number is valid according to the Luhn formula"""

# pylint: disable=missing-function-docstring

class Luhn: # pylint: disable=too-few-public-methods,missing-class-docstring
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isnumeric():
            return False

        digits = [int(char) for char in reversed(self.card_num)]

        checksum = sum(
            digit if index % 2 == 0 else
            digit * 2 if digit < 5 else
            digit * 2 - 9
            for index, digit in enumerate(digits)
        )
        
        return checksum % 10 == 0
