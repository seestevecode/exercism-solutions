"""Convert words and phrases to Pig Latin"""

import re

def translate_word(word):
    if re.match(r'[aeiou]|xr|yt', word):
        return word + 'ay'
    if match := re.match(r'([^aeiou]*qu)(.*)', word):
        return match.group(2) + match.group(1) + 'ay'
    if match := re.match(r'([^aeiou]+)(y.*)', word):
        return match.group(2) + match.group(1) + 'ay'
    if match := re.match(r'([^aeiou]+)(.*)', word):
        return match.group(2) + match.group(1) + 'ay'

def translate(text):
    return ' '.join(translate_word(word) for word in text.split(' '))
