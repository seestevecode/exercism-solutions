"""Compute the result for a game of Hex/Polygon"""

# pylint: disable=missing-function-docstring,missing-class-docstring

class ConnectGame:
    OFFSETS = (
        (-1,  0), (-1, 1),
        ( 0, -1), ( 0, 1),
        ( 1, -1), ( 1, 0)
    )
    
    def __init__(self, board):
        self.board = [row.replace(' ', '') for row in board.splitlines() if row]

    def _neighbours(self, row, col):
        return [
            (row + row_diff, col + col_diff)
            for row_diff, col_diff in self.OFFSETS
            if 0 <= row + row_diff < len(self.board)
            and 0 <= col + col_diff < len(self.board[row + row_diff])
        ]

    def _connected(self, player):
        if not self.board:
            return False
            
        if player == 'O':
            to_visit = [(0, col) for col, char in enumerate(self.board[0]) if char == 'O']
        elif player == 'X':
            to_visit = [(row, 0) for row, line in enumerate(self.board) if line[0] == 'X']
        else:
            raise ValueError('invalid player')

        visited = set()

        while to_visit:
            row, col = to_visit.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if player == 'O' and row == len(self.board) - 1:
                return True
            if player == 'X' and col == len(self.board[row]) - 1:
                return True
            to_visit.extend(
                (next_row, next_col)
                for next_row, next_col in self._neighbours(row, col)
                if self.board[next_row][next_col] == player
                and (next_row, next_col) not in visited
            )
            
        return False
                
    def get_winner(self):
        return 'O' if self._connected('O') else 'X' if self._connected('X') else ''
