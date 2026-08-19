def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')

    aliquot = sum(num for num in range(1, number // 2 + 1) if number % num == 0)

    return 'abundant' if number < aliquot else 'deficient' if number > aliquot else 'perfect'
