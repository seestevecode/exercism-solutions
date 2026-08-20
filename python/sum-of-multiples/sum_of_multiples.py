"""Calculate the sum of a set of unique multiples up to a limit"""

def sum_of_multiples(limit, multiples):
    return sum({
        num
        for multiple in multiples if multiple != 0
        for num in range(multiple, limit, multiple)
    })
