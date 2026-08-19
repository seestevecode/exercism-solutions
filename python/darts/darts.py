"""Calculate the points scored in a single toss of a Darts game"""

def score(x, y):
    square_dist = x ** 2 + y ** 2
    return (
        10 if square_dist <= 1 ** 2 else
        5 if square_dist <= 5 ** 2 else
        1 if square_dist <= 10 ** 2 else
        0
    )
