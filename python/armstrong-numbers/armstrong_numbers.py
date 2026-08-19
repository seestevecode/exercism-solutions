"""Function to determine if a number is an Armstrong number"""

def is_armstrong_number(number):
    digits = [int(num) for num in str(number)]
    num_digits = len(digits)
    return sum(digit ** num_digits for digit in digits) == number
