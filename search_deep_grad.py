from typing import List, Tuple
from model import Situation
from make_move import make_move


def generate_moves(situation, move_number):
    """
    Генерация возможных ходов для текущей ситуации.
    """
    return [0, 1, 2, 3]  # Возвращаем все возможные ходы (вверх, вправо, вниз, влево)


def manhattan(situation: Situation):
    manhattan_distance = 0
    board = situation.board
    size = len(board)
    for i in range(size):
        for j in range(size):
            tile = board[i][j]
            if tile != 0:
                target_row, target_col = (tile - 1) // size, (tile - 1) % size
                manhattan_distance += abs(i - target_row) + abs(j - target_col)

    return manhattan_distance


def search_depth_grad(init, MAX_DEPTH):
    stack = [(init, [])]
    visited = set()

    while stack:
        # Get current situation
        situation, path = stack.pop()

        # Check if the current situation is the goal
        if situation.board == situation.goal:
            return path

        # Marking the situation as viewed
        visited.add(tuple(situation.convertation(situation.board)))

        next_situations = list()

        for action in generate_moves(situation, len(path)):
            next_situation = make_move(situation, action)
            if next_situation and next_situation.isValid(*next_situation.position) and tuple(next_situation.convertation(next_situation.board)) not in visited:
                next_situations.append((next_situation, action))
        next_situations.sort(key=lambda x: manhattan(x[0]))

        # Generate new situations and add them to stack
        for data in next_situations:
            next_situation, action = data
            if len(stack) < MAX_DEPTH:
                stack.append((next_situation, path + [action]))

    # Solution doesn't find
    return None
