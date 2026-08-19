"""Create an implementation of the rotational cipher"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text, key):
    return ''.join(rotate_char(char, key) if char.isalpha() else char for char in text)


def rotate_char(char, key):
    rotated = ALPHABET[(ALPHABET.index(char.lower()) + key) % len(ALPHABET)]
    return rotated.upper() if char.isupper() else rotated
    