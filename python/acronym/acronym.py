"""Convert a phrase to its acronym"""

import re

def abbreviate(words):
    cleaned = re.sub(r'[^A-Z-\s]', '', words.upper())
    return ''.join(word[0] for word in re.split(r'[\s-]+', cleaned))
