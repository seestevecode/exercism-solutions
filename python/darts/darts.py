"""Calculate the points scored in a single toss of a Darts game"""

def score(x_dist, y_dist):
    square_dist = x_dist ** 2 + y_dist ** 2
    return (
        10 if square_dist <= 1 ** 2 else
        5 if square_dist <= 5 ** 2 else
        1 if square_dist <= 10 ** 2 else
        0
    )
