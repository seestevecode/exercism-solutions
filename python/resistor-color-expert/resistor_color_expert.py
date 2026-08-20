"""Converts a complex resistor to its value and label with tolerance"""

COLORS = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}

TOLERANCE = {
    'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
    'brown': 1, 'red': 2, 'gold': 5, 'silver': 10
}

VALUE_PREFIXES = {1_000_000_000: 'giga', 1_000_000: 'mega', 1_000: 'kilo'}

def resistor_label(colors):
    if len(colors) == 1:
        return '0 ohms'

    hundreds = 0 # needs initiating in case it doesn't have its own band
        
    if len(colors) == 4:
        tens, units, exponent = [COLORS[color] for color in colors[:3]]

    if len(colors) == 5:
        hundreds, tens, units, exponent = [COLORS[color] for color in colors[:4]]

    tolerance = TOLERANCE[colors[-1]]
    ohms = (100 * hundreds + 10 * tens + units) * 10 ** exponent

    for value, prefix in VALUE_PREFIXES.items():
        if ohms >= value:
            ohms /= value
            ohms_label = str(int(ohms) if ohms.is_integer() else ohms)
            return f'{ohms_label} {prefix}ohms ±{tolerance}%'

    return f'{ohms} ohms ±{tolerance}%'
