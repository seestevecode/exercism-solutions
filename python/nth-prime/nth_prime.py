"""Return the nth Prime Number"""

from itertools import count, islice
from math import isqrt

def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
        
    def is_prime(num):
        return all(num % divisor for divisor in range(2, isqrt(num) + 1))

    primes = (num for num in count(2) if is_prime(num))
    return next(islice(primes, number - 1, None))