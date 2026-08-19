"""Function to output a Raindrops string"""

DROPS = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

def convert(number):
    result = ''.join(drop for divisor, drop in DROPS.items() if number % divisor == 0)
    return result or str(number)
