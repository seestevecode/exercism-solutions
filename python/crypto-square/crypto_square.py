"""Encode text using a crypto square"""

# pylint: disable=missing-function-docstring

from math import isqrt

def cipher_text(plain_text):
    cleaned = ''.join(char.lower() for char in plain_text if char.isalnum())

    if not cleaned:
        return ''
        
    text_size = len(cleaned)
    rows = isqrt(text_size)
    cols = rows if rows * rows == text_size else rows + 1
    if rows * cols < text_size:
        rows += 1
    padded = cleaned.ljust(rows * cols, ' ')
    rows_text = [padded[idx:idx + cols] for idx in range(0, rows * cols, cols)]

    return ' '.join(''.join(column) for column in zip(*rows_text))
