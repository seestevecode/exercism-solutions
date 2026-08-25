"""Counts the number of occurrences of each word in a sentence"""

from collections import Counter
import re

def count_words(sentence):
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", sentence.lower()))
