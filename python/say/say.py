"""Express any number  up  to 1 trillion in words"""

LT20 = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
    'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

TENS = [
    'zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
    'sixty', 'seventy', 'eighty', 'ninety'
]

def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError('input out of range')
    
    if number < 20:
        return LT20[number]
    
    if number < 100:
        tens = number // 10
        units = number % 10
        return TENS[tens] + (f'-{LT20[units]}' if units else '')
    
    if number < 1_000:
        hundreds = number // 100
        rest = number % 100
        return say(hundreds) + ' hundred' + (' ' + say(rest) if rest else '')
    
    if number < 1_000_000:
        thousands = number // 1_000
        rest = number % 1_000
        return say(thousands) + ' thousand' + (' ' + say(rest) if rest else '')
    
    if number < 1_000_000_000:
        millions = number // 1_000_000
        rest = number % 1_000_000
        return say(millions) + ' million' + (' ' + say(rest) if rest else '')
    
    billions = number // 1_000_000_000
    rest = number % 1_000_000_000
    return say(billions) + ' billion' + (' ' + say(rest) if rest else '')
    