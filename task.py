# Автор: Малюков Д. И.
# Программа: Игра 15
# Описание: Данная программа реализует различные алгоритмы поиска пути для решения игры 15.
# Используются такие алгоритмы, как поиск в глубину и в ширину
# Версия: 17.10.2024

from print_header import print_header
from make_move import make_move
from model import Situation
from search_deep import search_depthr
from search_deep_grad import search_depth_grad
from solution import search_depth, generate_moves
from bfs import bfs

# создание игрового поля

def play_game():
    board = [[6, 8, 4],
             [3, 7, 2],
             [1, 5, 0]]

    init_pos = (2, 2)
    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]

    MAX_DEPTH = int(input("Введите максимальную глубину поиска: "))
    choice = "bfs"
    initial_situation = Situation(board, init_pos, goal)

    if choice == "dfs":
      solution = search_depth(initial_situation, MAX_DEPTH)
    elif choice == "dfs_grad":
      solution = search_depth_grad(initial_situation, MAX_DEPTH)
    elif choice == "bfs":
      solution = bfs(initial_situation)
      
    if solution:
        print(f"Решение найдено! Ходы: {solution}")
        print(f"Количество ходов: {len(solution)}")
    else:
        print("Решение не найдено.")


if __name__ == "__main__":
    print_header()
    play_game()
