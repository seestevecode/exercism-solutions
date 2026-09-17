"""Find the fewest number of coins to return a target from a list of denominations"""

# pylint: disable=missing-function-docstring

def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []

    fewest = [None] * (target + 1)
    fewest[0] = []

    for amount in range(1, target + 1):
        candidates = [
            fewest[amount - coin] + [coin]
            for coin in coins
            if coin <= amount
            and fewest[amount - coin] is not None
        ]

        if candidates:
            fewest[amount] = min(candidates, key=len)

    if fewest[target] is None:
        raise ValueError("can't make target with given coins")

    return sorted(fewest[target])
