from model import Situation
from make_move import make_move

def generate_moves(situation, move_number):
    """
    Генерация возможных ходов для текущей ситуации.
    """
    return [0, 1, 2, 3]  # Возвращаем все возможные ходы (вверх, вправо, вниз, влево)


def search_depth(init, MAX_DEPTH):
    """
    Performs Depth-First Search (DFS) to find a solution to the 15-puzzle.

    Args:
        init: The initial situation of the puzzle as a 2D list.
        init_pos: The position of the empty tile in the initial situation as a tuple.
        goal: The goal situation of the puzzle.
        MAX_DEPTH: The maximum depth of the search.

    Returns:
        A list of actions (0-3, representing up, down, left, right) that lead to the goal situation,
        or None if no solution is found within the specified depth.
    """
    
    init_pos = (2, 2)
    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]

    # Initializing the initial situation
    init_situation = Situation(init, init_pos, goal)
        
    stack = [(init_situation, [])]
    visited = set()
    move_number = 0

    while stack:

        # Get current situation
        situation, path = stack.pop()

        # Check goal
        if situation.is_solved():
            print("Конечное поле:")
            situation.print_board()
            return path

        # Marking the situation as viewed
        visited.add(tuple(situation.convertation(situation.board)))

        # Generate new situations and add its to stack
        for action in generate_moves(situation, len(path)):  # Передача move_number (len(path))
            next_situation = make_move(situation, action)
            if len(path) < MAX_DEPTH and next_situation and next_situation.isValid(*next_situation.position) and \
                    tuple(next_situation.convertation(next_situation.board)) not in visited:
                #print("Промежуточное поле:")
                #next_situation.print_board()
                stack.append((next_situation, path + [action]))
                move_number += 1  # Увеличиваем move_number при добавлении в стек

    # Solution doesn't find
    return None