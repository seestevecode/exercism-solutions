"""Output the content of the poem, The House That Jack Built"""

NOUN_VERBS = {
    2: ('malt', 'lay in'),
    3: ('rat', 'ate'),
    4: ('cat', 'killed'),
    5: ('dog', 'worried'),
    6: ('cow with the crumpled horn', 'tossed'),
    7: ('maiden all forlorn', 'milked'),
    8: ('man all tattered and torn', 'kissed'),
    9: ('priest all shaven and shorn', 'married'),
    10: ('rooster that crowed in the morn', 'woke'),
    11: ('farmer sowing his corn', 'kept'),
    12: ('horse and the hound and the horn', 'belonged to')
}

def recite_verse(verse):
    if verse == 1:
        return 'This is the house that Jack built.'

    result = 'This is '
    
    for num in range(verse, 1, -1):
        noun, verb = NOUN_VERBS[num]
        result += f'the {noun} that {verb} '
        
    result += 'the house that Jack built.'
    return result
        

def recite(start_verse, end_verse):
    return [recite_verse(verse) for verse in range(start_verse, end_verse + 1)]
