"""Implement the Sieve of Eratosthenes"""

# pylint: disable=missing-function-docstring

def primes(limit):
    numbers = set(range(2, limit + 1))
    composites = {num for number in numbers for num in range(2 * number, limit + 1, number)}
    return sorted(numbers - composites)
