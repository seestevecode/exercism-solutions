"""Recite specified verses of Ten Green Bottles"""

# pylint: disable=missing-function-docstring

NUMBERS = (
    'no', 'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine', 'ten'
)


def recite_verse(num):
    def plural(bottles):
        return '' if bottles == 1 else 's'

    return [
        f'{NUMBERS[num]} green bottle{plural(num)} hanging on the wall,'.capitalize(),
        f'{NUMBERS[num]} green bottle{plural(num)} hanging on the wall,'.capitalize(),
        'And if one green bottle should accidentally fall,',
        f"There'll be {NUMBERS[num - 1]} green bottle{plural(num - 1)} hanging on the wall."
    ]

def recite(start, take=1):
    result = []
    
    for index, verse in enumerate(range(start, start - take, -1)):
        result.extend(recite_verse(verse))
        if index < take - 1:
            result.append('')

    return result
