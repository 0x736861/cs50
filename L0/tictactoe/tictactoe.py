"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


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
    count_EMPTY = sum(row.count(EMPTY) for row in board)
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    if count_EMPTY == 9 or count_X == count_O:
        return X
    elif count_X > count_O:
        return O
    else:
        return X if count_X < count_O else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                actions_set.add((row, col))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        return copy.deepcopy(board)

    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action", action)

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            return X
        if all(board[row][col] == O for row in range(3)):
            return O

    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        return X
    if all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    best_action, _ = do_minimax(board, 0)
    return best_action


def do_minimax(board, depth):
    """
    Returns the optimal action for the current player on the board.
    """

    max_depth = 9
    print('minmax with board:', board)

    best_action = None

    if terminal(board) or depth > max_depth:
        res = utility(board)
        return None, res

    if player(board) == X:

        print('\nturning X')
        best_value = -math.inf
        print(best_value, best_action)

        for action in actions(board):
            print('action', action)

            board_with_action = result(board, action)
            print('board_with_action', board_with_action)

            move_action, move_value = do_minimax(board_with_action, depth + 1)
            print('move_value:', move_value)

            if move_value is None:
                continue

            if move_value is not None and move_value > best_value:
                best_value = move_value
                best_action = action
                print('best_value updated:', best_value, 'best_action updated:', best_action)

    else:
        print('\nturning O')

        best_value = math.inf
        print(best_value, best_action)

        all_actions = actions(board)
        print('all_actions', all_actions)
        for action in all_actions:
            print('action', action)

            board_with_action = result(board, action)
            print('board_with_action', board_with_action)

            move_action, move_value = do_minimax(board_with_action, depth + 1)
            print('move_value:', move_value)

            if move_value is None:
                continue

            if move_value is not None and move_value < best_value:
                best_value = move_value
                best_action = action
                print('best_value updated:', best_value, 'best_action updated:', best_action)

    return best_action, best_value
