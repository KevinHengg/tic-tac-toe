"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
curr_player = ""

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    placed = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                placed += 1
    if placed % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x, y) = action
    temp = copy.deepcopy(board)
    if temp[x][y] == EMPTY:
        temp[x][y] = player(board)
    else:
        raise Exception('Action not valid')
    return temp


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1]) & (board[i][0] == board[i][2]) & (board[i][0] != EMPTY):
            return board[i][0]
        elif (board[0][i] == board[1][i]) & (board[0][i] == board[2][i]) & (board[0][i] != EMPTY):
            return board[0][i]
        else:
            return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if terminal return none
    if terminal(board):
        return None

    optimal = 0
    possible_actions = actions(board)
    v = 0
    
    # for each possible actions
    for i in range(len(possible_actions)):
        temp_board = board
        temp_board = result(temp_board, possible_actions[i])
        if player(board) == X:
            val = x_max(temp_board)
            if val >= v:
                v = val
                optimal = possible_actions[i]
        else: 
            val = o_min(temp_board)
            if v >= val:
                v = val
                optimal = possible_actions[i]
    return optimal

def x_max(board):

    if terminal(board):
        return utility(board)
    v = -math.inf
    # for each possible action
    for i in range(len(actions(board))):
        temp_board = board
        # resulting board
        temp_board = result(temp_board, actions(board)[i])
        val = o_min(temp_board)
        if val >= v:
            v = val
    return v
    
def o_min(board):

    if terminal(board):
        return utility(board)
    v = math.inf
    # for each possible action
    for i in range(len(actions(board))):
        temp_board = board
        # resulting board
        temp_board = result(temp_board, actions(board)[i])
        val = x_max(temp_board)
        if val < v:
            v = val
    return v