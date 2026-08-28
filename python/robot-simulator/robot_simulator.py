"""Simulate a robot's turns and movements"""

# pylint: disable=missing-function-docstring

EAST = 90
NORTH = 0
WEST = 270
SOUTH = 180

ADVANCES = {NORTH: (0, 1), EAST: (1, 0), SOUTH: (0, -1), WEST: (-1, 0)}

class Robot:  # pylint: disable=too-few-public-methods,missing-class-docstring
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction

    def move(self, instruction_list):
        for instruction in instruction_list:
            if instruction == 'R':
                self.direction = (self.direction + 90) % 360
            elif instruction == 'L':
                self.direction = (self.direction - 90) % 360
            elif instruction == 'A':
                coord_x, coord_y = self.coordinates
                delta_x, delta_y = ADVANCES[self.direction]
                self.coordinates = (coord_x + delta_x, coord_y + delta_y)
        