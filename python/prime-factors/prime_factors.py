"""Return all prime factors of a given value"""

def factors(value):
    prime_factors = []
    candidate = 2
    remaining = value

    while remaining > 1:
        if remaining % candidate == 0:
            prime_factors.append(candidate)
            remaining //= candidate
        else:
            candidate = 3 if candidate == 2 else candidate + 2

    return prime_factors
    