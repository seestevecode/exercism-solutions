"""Find the best poker hand(s) from a list of hands"""

from collections import Counter

RANKS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

def hand_value(hand):
    """Values the hand and returns tuple with relative weight, values and kickers"""
    
    # parse hand into ranks and suits
    cards = hand.split()
    ranks = [RANKS[card[:-1]] for card in cards]
    suits = [card[-1] for card in cards]

    # count cards per rank
    counts = Counter(ranks)
    groups = sorted(
        ((count, rank) for rank, count in counts.items()),
        reverse=True
    )

    unique_ranks = sorted(set(ranks))

    # establish if hand is a straight and get the high card
    if unique_ranks == [2, 3, 4, 5, 14]:
        straight_high = 5
    elif (
        len(unique_ranks) == 5
        and unique_ranks[-1] - unique_ranks[0] == 4
    ):
        straight_high = unique_ranks[-1]
    else:
        straight_high = None  # not a straight

    # establish if hand is flush
    flush = len(set(suits)) == 1

    # straight flush with high card
    if straight_high and flush:
        return 8, straight_high

    # four of a kind with four-value kicker
    if groups[0][0] == 4:
        return 7, groups[0][1], groups[1][1]

    # full house with three-value and two-value
    if [count for count, _rank in groups] == [3, 2]:
        return 6, groups[0][1], groups[1][1]

    # flush with ranks high first
    if flush:
        return 5, *sorted(ranks, reverse=True)

    # straight with high card
    if straight_high:
        return 4, straight_high

    # three of a kind with three-value and kickers
    if groups[0][0] == 3:
        triple = groups[0][1]
        kickers = sorted(
            (rank for rank in ranks if rank != triple),
            reverse=True
        )
        return 3, triple, *kickers

    # pair/s within hand
    pairs = sorted(
        (rank for rank, count in counts.items() if count == 2),
        reverse=True
    )

    # two pairs with kicker
    if len(pairs) == 2:
        kicker = next(
            rank for rank, count in counts.items() if count == 1
        )
        return 2, *pairs, kicker

    # single pair with kickers
    if len(pairs) == 1:
        pair = pairs[0]
        kickers = sorted(
            (rank for rank in ranks if rank != pair),
            reverse=True
        )
        return 1, pair, *kickers

    # cards returned high first
    return 0, *sorted(ranks, reverse=True)
    

def best_hands(hands):
    """Compare all hands and return the best"""
    values = [(hand_value(hand), hand) for hand in hands]
    best = max(value for value, _hand in values)

    return [hand for value, hand in values if value == best]
