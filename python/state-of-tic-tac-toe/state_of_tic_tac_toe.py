"""Determine the state of a game of Tic-Tac-Toe (Noughts and Crosses)"""

def transposed(board):
    """Transpose the board"""
    return [''.join(row) for row in zip(*board)]
    

def row_win(board, player):
    """Return true if player has a row on the board"""
    return any(row == 3 * player for row in board)


def diag_win(board, player):
    """Return true if player has a diagonal on the board"""
    
    def is_winning_diag(board):
        """Return true if player has leading diagonal - top-left to bottom-right"""
        return ''.join(board[index][index] for index in range(3)) == 3 * player

    flipped = [row[::-1] for row in board]
    return any(is_winning_diag(candidate) for candidate in (board, flipped))


def gamestate(board):
    """Return the gamestate of the board, including any errors"""
    
    o_pieces, x_pieces, spaces = [''.join(board).count(square) for square in 'OX ']
    transposed_board = transposed(board)
    x_win = row_win(board, 'X') or row_win(transposed_board, 'X') or diag_win(board, 'X')
    o_win = row_win(board, 'O') or row_win(transposed_board, 'O') or diag_win(board, 'O')

    if o_pieces > x_pieces:
        raise ValueError('Wrong turn order: O started')

    if x_pieces - o_pieces > 1:
        raise ValueError('Wrong turn order: X went twice')
    
    if (  # pylint: disable=too-many-boolean-expressions
        (x_win and o_win)  # both have won
        or (x_win and x_pieces == o_pieces)  # O has moved after X won
        or (o_win and x_pieces > o_pieces)  # X has moved after O won
    ):
        raise ValueError('Impossible board: game should have ended after the game was won')

    if x_win or o_win:
        return 'win'

    if spaces == 0:
        return 'draw'

    return 'ongoing'
    