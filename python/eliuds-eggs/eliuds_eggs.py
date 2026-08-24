"""Count the number of 1s in the binary representation of a number"""

def egg_count(display_value):
    return (
        display_value 
        if display_value < 2 
        else (display_value % 2) + egg_count(display_value // 2)
    )
