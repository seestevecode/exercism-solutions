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
    verses = [recite_verse(verse) for verse in range(start, start - take, -1)]
    return [
        line
        for verse_idx, verse in enumerate(verses)
        for line in verse + ([''] if verse_idx < len(verses) - 1 else [])
    ]  
