"""Manage robot factory settings"""

import random
import string

def random_name():
    """Assign a random name in the format, e.g. AB123"""
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=3))
    return letters + digits

class Robot: # pylint: disable=missing-class-docstring
    _used_names = set()
    
    def __init__(self):
        """Initiate a new robot"""
        self._name = None

    @property
    def name(self):
        """Give a robot an unused name"""
        if self._name is None:
            while True:
                candidate = random_name()
                if candidate not in Robot._used_names:
                    Robot._used_names.add(candidate)
                    self._name = candidate
                    break

        return self._name

    def reset(self):
        """Reset the robot's name"""
        self._name = None
