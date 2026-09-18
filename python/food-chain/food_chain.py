"""Recite verses from the poem 'I Know an Old Lady Who Swallowed a Fly'"""

# pylint: disable=missing-function-docstring

CHAIN = (
    ('fly', "I don't know why she swallowed the fly. Perhaps she'll die."),
    ('spider', 'It wriggled and jiggled and tickled inside her.'),
    ('bird', 'How absurd to swallow a bird!'),
    ('cat', 'Imagine that, to swallow a cat!'),
    ('dog', 'What a hog, to swallow a dog!'),
    ('goat', 'Just opened her throat and swallowed a goat!'),
    ('cow', "I don't know how she swallowed a cow!"),
    ('horse', None)
)

def recite_verse(verse_num):
    verse = [f'I know an old lady who swallowed a {CHAIN[verse_num - 1][0]}.']
    
    if verse_num == 8:
        return verse + ["She's dead, of course!"]
        
    if verse_num > 1:
        verse.append(CHAIN[verse_num - 1][1])
        for index in range(verse_num, 1, -1):
            predator = CHAIN[index - 1][0]
            prey = CHAIN[index - 2][0]
            swallowed = f'She swallowed the {predator} to catch the {prey}.'
            if prey == 'spider':
                swallowed = swallowed.replace(
                    'spider',
                    'spider that wriggled and jiggled and tickled inside her'
                )
            verse.append(swallowed)
            
    verse.append(CHAIN[0][1])
    return verse


def recite(start_verse, end_verse):
    poem = []
    for verse in range(start_verse, end_verse + 1):
        poem.extend(recite_verse(verse))
        poem.append('')
            
    return poem[:-1]
