"""Find all Pythagorean Triplets adding up to a specified number"""

# pylint: disable=missing-function-docstring

def is_triplet(a, b, c):
    return a**2 + b**2 == c**2 and a < b < c


def triplets_with_sum(number):
    result = []

    # Running a single loop keeps the solution O(n)
    # Since a < b < c, a must be less than one third of the total.
    for a in range(1, number // 3):
        # From a + b + c = n and a² + b² = c²:
        # b = n(n - 2a) / 2(n - a)
        numerator = number * (number - 2 * a)
        denominator = 2 * (number - a)

        # b must be an integer.
        if numerator % denominator == 0:
            b = numerator // denominator
            c = number - a - b

            if is_triplet(a, b, c):
                result.append([a, b, c])

    return result
