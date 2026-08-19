"""Function to calculate the number of steps in the Collatz conjecture"""

def steps(number):
    if number < 1:
        raise ValueError('Only positive integers are allowed')
    return (
        0 if number == 1 
        else 1 + steps(number // 2 if number % 2 == 0 else number * 3 + 1)
    )
