from print_header import print_header
from make_move import make_move
from model import Situation
from search_deep import search_depth, generate_moves

# Автор: Малюков Д. И.
# Программа: Игра 15
# Описание: Данная программа реализует различные алгоритмы поиска пути для решения игры 15.
# Используются такие алгоритмы, как поиск в глубину и в ширину
# Версия: 08.10.2024

# создание игрового поля
def play_game():
    init_situation = [[6, 8, 4],
                     [3, 7, 2],
                     [1, 5, 0]]
    

    MAX_DEPTH = int(input("Введите максимальную глубину поиска: "))
    
    solution = search_depth(init_situation, MAX_DEPTH)

    if solution:
        print(f"Решение найдено! Ходы: {solution}")
        print(f"Количество ходов: {len(solution)}")
    else:
        print("Решение не найдено.")


if __name__ == "__main__":
    print_header()
    play_game()