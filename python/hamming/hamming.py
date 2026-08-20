"""Calculate Hamming distance between two strands"""

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')

    return sum(1 for index, value in enumerate(strand_a) if value != strand_b[index])
