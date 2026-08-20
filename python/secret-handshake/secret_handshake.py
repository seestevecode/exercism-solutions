"""Decode a binary string into a list of commands for a secret handshake"""

COMMANDS = ['reverse', 'jump', 'close your eyes', 'double blink', 'wink']

def commands(binary_str):
    command_list = [
        cmnd for str_bit, cmnd in zip(list(binary_str), COMMANDS) 
        if str_bit == '1'
    ]
    return (
        command_list if command_list == [] else
        command_list[1:] if command_list[0] == 'reverse' 
        else command_list[::-1]
    )
