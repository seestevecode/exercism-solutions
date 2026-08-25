"""Implement Run Length Encoding and Decoding"""

from itertools import groupby
import re

def decode(string):
    pairs = re.findall(r'(\d+)?(\D)', string)

    return ''.join(
        (int(count) if count else 1) * char
        for count, char in pairs
    )
    

def encode(string):
    def encode_group(letter, chars):
        count = sum(1 for _ in chars)
        return (str(count) if count > 1 else '') + letter

    return ''.join(
        encode_group(letter, chars)
        for letter, chars in groupby(string)
    )
    