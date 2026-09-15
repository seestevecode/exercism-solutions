"""Implement the Vigenere cipher"""

# pylint: disable=missing-function-docstring

import secrets

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class Cipher:  # pylint: disable=missing-class-docstring
    def __init__(self, key=None):
        self.key = key or ''.join(secrets.choice(ALPHABET) for _idx in range(100))

    def _translate(self, text, direction):
        def translate_char(index, char):
            char_index = ALPHABET.index(char)
            key_char = self.key[index % len(self.key)]
            shift = ALPHABET.index(key_char)
    
            return ALPHABET[(char_index + direction * shift) % 26]

        return ''.join(translate_char(index, char) for index, char in enumerate(text))

    def encode(self, text):
        return self._translate(text, 1)

    def decode(self, text):
        return self._translate(text, -1)
