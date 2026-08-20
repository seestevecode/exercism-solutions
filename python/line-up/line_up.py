"""Produce a sentence using name, number and the number's ordinal"""

def line_up(name, number):
    ordinal = (
        'st' if number % 10 == 1 and number % 100 != 11 else
        'nd' if number % 10 == 2 and number % 100 != 12 else
        'rd' if number % 10 == 3 and number % 100 != 13 else
        'th'
    )
    return f'{name}, you are the {number}{ordinal} customer we serve today. Thank you!'
