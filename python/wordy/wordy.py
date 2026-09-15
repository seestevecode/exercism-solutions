"""Implement a parser and tokeniser for string calculations"""

# pylint: disable=missing-function-docstring

OPERATIONS = {
    'plus': lambda a, b: a + b,
    'minus': lambda a, b: a - b,
    'multiplied': lambda a, b: a * b,
    'divided': lambda a, b: a / b,
}

def parse_number(token):
    try:
        return int(token)
    except ValueError:
        raise ValueError('syntax error') from None
        

def answer(question):
    cleaned = (
        question
        .removeprefix('What is ')
        .removesuffix('?')
        .replace('multiplied by', 'multiplied')
        .replace('divided by', 'divided')
        .split()
    )

    result = parse_number(cleaned[0])
    remaining = cleaned[1:]

    while remaining:
        operation = remaining[0]

        if operation.lstrip('-').isdigit():
            raise ValueError('syntax error')

        if operation not in OPERATIONS:
            raise ValueError('unknown operation')

        if len(remaining) < 2:
            raise ValueError('syntax error')

        operand = parse_number(remaining[1])
        result = OPERATIONS[operation](result, operand)
        remaining = remaining[2:]
    
    return result
