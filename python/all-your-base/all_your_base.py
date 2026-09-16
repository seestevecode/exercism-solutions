"""Convert a sequence of digits from one base to another base"""

# pylint: disable=missing-function-docstring

def from_digits(digits, input_base):
    result = 0
    for digit in digits:
        result = result * input_base + digit
    return result


def to_digits(number, output_base):
    if number == 0:
        return [0]
        
    digits = []
    while number > 0:
        number, digit = divmod(number, output_base)
        digits.append(digit)

    return digits[::-1]
        

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError('all digits must satisfy 0 <= d < input base')

    return (
        [0] if not digits else 
        to_digits(from_digits(digits, input_base), output_base)
    )

# adapted from Clojure solution to same puzzle
