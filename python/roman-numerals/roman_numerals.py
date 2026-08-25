"""Convert Arabic numbers to their Roman numeral equivalent"""

ARABIC_ROMAN = (
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
)

def roman(number):
    symbols = []

    for value, symbol in ARABIC_ROMAN:
        count, number = divmod(number, value)
        symbols.append(symbol * count)
    
    return ''.join(symbols)
