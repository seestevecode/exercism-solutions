"""Implement a clock that handles times without dates"""

# pylint: disable=missing-function-docstring,missing-class-docstring

class Clock:
    def __init__(self, hour, minute):
        raw_minutes = (hour * 60 + minute) % (24 * 60)
        self.hour = raw_minutes // 60
        self.minute = raw_minutes % 60

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
