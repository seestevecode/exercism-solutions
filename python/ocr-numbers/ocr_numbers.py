"""Convert an OCR grid to a string of digits"""

# pylint: disable=missing-function-docstring

NUMBERS = {
    (' _ ', '| |', '|_|', '   '): '0',
    ('   ', '  |', '  |', '   '): '1',
    (' _ ', ' _|', '|_ ', '   '): '2',
    (' _ ', ' _|', ' _|', '   '): '3',
    ('   ', '|_|', '  |', '   '): '4',
    (' _ ', '|_ ', ' _|', '   '): '5',
    (' _ ', '|_ ', '|_|', '   '): '6',
    (' _ ', '  |', '  |', '   '): '7',
    (' _ ', '|_|', '|_|', '   '): '8',
    (' _ ', '|_|', ' _|', '   '): '9',
}

def convert(input_grid):
    height = len(input_grid)
    width = len(input_grid[0]) if input_grid else 0

    if height % 4:
        raise ValueError('Number of input lines is not a multiple of four')
    if width % 3:
        raise ValueError('Number of input columns is not a multiple of three')

    def decode_digit(digit_row, digit_col):
        return NUMBERS.get(
            tuple(grid_row[digit_col:digit_col + 3] 
                  for grid_row in input_grid[digit_row:digit_row + 4]),
            '?'
        )
        
    return ','.join(
        ''.join(decode_digit(row, col) for col in range(0, width, 3))
        for row in range(0, height, 4)
    )
