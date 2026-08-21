"""Implement the Atbash Cipher functions to encode and decode"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'

CIPHER = dict(zip(ALPHABET + NUMBERS, ALPHABET[::-1] + NUMBERS))

def encode(plain_text):
    encoded = ''.join(CIPHER[char.lower()] for char in plain_text if char.isalnum())
    return ' '.join(encoded[index:index + 5] for index in range(0, len(encoded), 5))


def decode(ciphered_text):
    return ''.join(CIPHER[char] for char in ciphered_text if char.isalnum())
