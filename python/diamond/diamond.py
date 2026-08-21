"""Output a Diamond shape starting with A 
and having the supplied letter at its widest point"""

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def diamond_row(letter, columns):
    return ''.join(letter if letter == column else ' ' for column in columns)
        

def rows(letter):
    letters = ALPHABET[:ALPHABET.index(letter) + 1]
    row_letters = letters + letters[-2::-1]
    columns = letters[::-1] + letters[1:]

    return [diamond_row(row_letter, columns) for row_letter in row_letters]
