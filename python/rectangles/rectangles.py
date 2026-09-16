"""Count the rectangles in an ASCII diagram"""

# pylint: disable=missing-function-docstring

def rectangles(strings):
    def valid_horizontal(row, left_col, right_col):
        return all(
            char in '-+' 
            for char in strings[row][left_col + 1:right_col]
        )

    def valid_vertical(column, top_row, bottom_row):
        return all(
            strings[row][column] in '|+' 
            for row in range(top_row + 1, bottom_row)
        )
    
    corners = [
        (row_num, col_num)
        for row_num, string in enumerate(strings)
        for col_num, char in enumerate(string)
        if char == '+'
    ]
    
    top_pairs = [
        (top_left, top_right)
        for top_left in corners
        for top_right in corners
        if top_left[0] == top_right[0] and top_left[1] < top_right[1]
    ]

    rectangle_count = 0
    
    for top_left, top_right in top_pairs:
        bottom_pairs = [
            (bottom_left, bottom_right)
            for bottom_left, bottom_right in top_pairs
            if bottom_left[0] > top_left[0] 
            and bottom_left[1] == top_left[1] 
            and bottom_right[1] == top_right[1]
        ]

        for bottom_left, bottom_right in bottom_pairs:            
            if (
                valid_horizontal(top_left[0], top_left[1], top_right[1]) 
                and valid_horizontal(bottom_left[0], bottom_left[1], bottom_right[1])
                and valid_vertical(top_left[1], top_left[0], bottom_left[0])
                and valid_vertical(top_right[1], top_right[0], bottom_right[0])
            ):
                rectangle_count += 1

    return rectangle_count
