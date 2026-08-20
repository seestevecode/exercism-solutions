"""Convert a 3-band resistor to its value with a label"""

COLORS = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}

VALUE_PREFIXES = {1_000_000_000: 'giga', 1_000_000: 'mega', 1_000: 'kilo'}

def label(colors):
    tens, units, exponent, *_ = [COLORS[color] for color in colors]
    ohms = (10 * tens + units) * 10 ** exponent

    for value, prefix in VALUE_PREFIXES.items():
        if ohms > value:
            return f'{ohms // value} {prefix}ohms'

    return f'{ohms} ohms'
    