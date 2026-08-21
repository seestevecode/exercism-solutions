"""Check for correctly nested bracket pairs"""

BRACKET_PAIRS = {'[': ']', '(': ')', '{': '}'}

def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in BRACKET_PAIRS:
            stack.append(char)
        elif char in BRACKET_PAIRS.values():
            if not stack or char != BRACKET_PAIRS[stack.pop()]:
                return False

    return not stack
