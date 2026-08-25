"""Return the lyrics of the song The Twelve Days of Christmas"""

GIFTS = (
    '',
    'a Partridge in a Pear Tree',
    'two Turtle Doves',
    'three French Hens',
    'four Calling Birds',
    'five Gold Rings',
    'six Geese-a-Laying',
    'seven Swans-a-Swimming',
    'eight Maids-a-Milking',
    'nine Ladies Dancing',
    'ten Lords-a-Leaping',
    'eleven Pipers Piping',
    'twelve Drummers Drumming'
)

ORDINALS = (
    '', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
    'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
)

def recite_verse(verse_num):
    gifts = [GIFTS[index] for index in range(verse_num, 0, -1)]
    if verse_num > 1:
        gifts[-1] = f'and {gifts[-1]}'

    return (
        f'On the {ORDINALS[verse_num]} day of Christmas my true love gave to me: '
        f'{", ".join(gifts)}.'
    )

    
def recite(start_verse, end_verse):
    return [recite_verse(num) for num in range(start_verse, end_verse + 1)]
