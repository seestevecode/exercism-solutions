"""Generate a Dungeons and Dragons character"""

# pylint: disable=missing-function-docstring

import random

ABILITIES = (
    'strength', 'dexterity', 'constitution',
    'intelligence', 'wisdom', 'charisma')

def modifier(score):
    return (score - 10) // 2


class Character: # pylint: disable=missing-class-docstring,too-few-public-methods
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        dice = sorted(random.randint(1, 6) for _die in range(4))
        return sum(dice[1:])
