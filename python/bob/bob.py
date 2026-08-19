"""Function to construct Bob's responses to stimulus"""

def is_shouting(string):
    letters = [char for char in string if char.isalpha()]
    return letters and string.upper() == string

def response(hey_bob):
    stripped_bob = hey_bob.strip()
    if is_shouting(stripped_bob) and stripped_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if stripped_bob == '' or stripped_bob.isspace():
        return 'Fine. Be that way!'
    if stripped_bob.endswith('?'):
        return 'Sure.'
    if is_shouting(stripped_bob):
        return 'Whoa, chill out!'
    return 'Whatever.'
