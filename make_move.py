from model import Situation
import copy


n = 4
ACTIONS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

def make_move(situation, action):
    """
    Делает ход в игре пятнашки.
    """
    empty_row, empty_col = situation.position

    new_board = [row[:] for row in situation.board]  # Создаем копию

    if action == 0 and empty_row > 0:  # Вверх
        new_board[empty_row][empty_col] = new_board[empty_row - 1][empty_col]
        new_board[empty_row - 1][empty_col] = 0
        return Situation(new_board, (empty_row - 1, empty_col), situation.goal)
    elif action == 1 and empty_col < len(situation.board[0]) - 1:  # Вправо
        new_board[empty_row][empty_col] = new_board[empty_row][empty_col + 1]
        new_board[empty_row][empty_col + 1] = 0
        return Situation(new_board, (empty_row, empty_col + 1), situation.goal)
    elif action == 2 and empty_row < len(situation.board) - 1:  # Вниз
        new_board[empty_row][empty_col] = new_board[empty_row + 1][empty_col]
        new_board[empty_row + 1][empty_col] = 0
        return Situation(new_board, (empty_row + 1, empty_col), situation.goal)
    elif action == 3 and empty_col > 0:  # Влево
        new_board[empty_row][empty_col] = new_board[empty_row][empty_col - 1]
        new_board[empty_row][empty_col - 1] = 0
        return Situation(new_board, (empty_row, empty_col - 1), situation.goal)

    return None
