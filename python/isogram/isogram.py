"""Determine if a word or phrase contains no repeated letters"""

def is_isogram(phrase):
    cleaned = [char for char in phrase.lower() if char.isalpha()]
    return len(set(cleaned)) == len(cleaned)
