"""Figure out if a sentence contains every letter of the Latin alphabet"""

def is_pangram(sentence):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(sentence.lower())
