"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the time to prepare the lasagna.

    Parameters:
        number_of_layers (int): The number of layers to the lasagna.

    Returns:
        int: The time to prepare the cake (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers to the lasagna as
    an argument and returns how many minutes the lasagna needs to prepare it
    based on the `PREPARATION_TIME`.
    """
    
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time so far since preparation started.

    Parameters:
        number_of_layers (int): The number of layers to the lasagna.
        elapsed_bake_time (int): Time the lasagna has been in the oven so far.

    Returns:
        int: The time to since preparation started.

    Function that takes the number of layers to the lasagna and the time it's been
    in the overn so far as arguments, and returns how many minutes the lasagna
    it's been since preparation started.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
