"""Implement the Vigenere cipher"""

# pylint: disable=missing-function-docstring

import secrets

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class Cipher:  # pylint: disable=missing-class-docstring
    def __init__(self, key=None):
        self.key = key or ''.join(secrets.choice(ALPHABET) for _idx in range(100))

    def _translate(self, text, direction):
        return ''.join(
            ALPHABET[
                (
                    ALPHABET.index(char)
                    + direction * ALPHABET.index(self.key[index % len(self.key)])
                )
                % 26
            ]
            for index, char in enumerate(text)
        )

    def encode(self, text):
        return self._translate(text, 1)

    def decode(self, text):
        return self._translate(text, -1)
