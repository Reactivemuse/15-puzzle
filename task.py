# Автор: Малюков Д. И.
# Программа: Игра 15
# Описание: Данная программа реализует различные алгоритмы поиска пути для решения игры 15.
# Используются такие алгоритмы, как поиск в глубину и в ширину
# Версия: 08.10.2024

def print_header():
    print("##############################################")
    print("# Author: Малюков Дмитрий Иванович")
    print("# Program: 15 Puzzle Solver")
    print(
        "# Description: This program implements various search algorithms to solve the 15-puzzle. "
    )
    print("# The program utilizes Depth-First Search (DFS) and Breadth-First Search (BFS) to find the optimal solution.")
    print("# Version: 08.10.2024")
    print("##############################################")
class Situation:
    def __init__(self, board, position, goal):
        self.board = board
        self.position = position
        self.goal = goal

    def is_solved(self):
        return self.board == self.goal

    def isValid(self, row, col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def convert_to_line(self, board):
        return [num for row in board for num in row]

    def print_board(self):
        for row in self.board:
            for num in row:
                print(num, end=" ")
            print()
        print("-" * 15)

# порождающая функция
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


def generate_moves(situation, move_number):
    """
    Генерация возможных ходов для текущей ситуации.
    """
    return [0, 1, 2, 3]  # Возвращаем все возможные ходы (вверх, вправо, вниз, влево)


def dfs(initial, initial_pos, goal, MAX_DEPTH):
    """
    Performs Depth-First Search (DFS) to find a solution to the 15-puzzle.

    Args:
        initial: The initial state of the puzzle as a 2D list.
        initial_pos: The position of the empty tile in the initial state as a tuple.
        goal: The goal state of the puzzle.
        MAX_DEPTH: The maximum depth of the search.

    Returns:
        A list of actions (0-3, representing up, down, left, right) that lead to the goal state,
        or None if no solution is found within the specified depth.
    """

    # Initializing the initial situation
    initial_situation = Situation(initial, initial_pos, goal)
    stack = [(initial_situation, [])]
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
        visited.add(tuple(situation.convert_to_line(situation.board)))

        # Generate new situations and add its to stack
        for action in generate_moves(situation, len(path)):  # Передача move_number (len(path))
            next_state = make_move(situation, action)
            if len(path) < MAX_DEPTH and next_state and next_state.isValid(*next_state.position) and \
                    tuple(next_state.convert_to_line(next_state.board)) not in visited:
                #print("Промежуточное поле:")
                #next_state.print_board()
                stack.append((next_state, path + [action]))
                move_number += 1  # Увеличиваем move_number при добавлении в стек

    # Solution doesn't find
    return None

# создание игрового поля
def play_game():
    initial_state = [[6, 8, 4],
                     [3, 7, 2],
                     [1, 5, 0]]
    initial_pos = (2, 2)
    goal_state = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]

    solution = dfs(initial_state, initial_pos, goal_state, 100)

    if solution:
        print(f"Решение найдено! Ходы: {solution}")
        print(f"Количество ходов: {len(solution)}")
    else:
        print("Решение не найдено.")


if __name__ == "__main__":
    print_header()
    play_game()