from model import Situation
from make_move import make_move

def search_depthr(current_situation, path = [], stack = []):
    """
    Рекурсивный поиск в глубину (Depth-First Search) в игре "Волк, коза и капуста".
    
    :param current_situation: текущая ситуация игры
    :param path: путь действий, ведущий к текущей ситуации
    :return: список действий, приводящий к целевой ситуации, или None, если решение не найдено
    """
    if not stack:
        stack = [current_situation]

    # Проверяем, достигнута ли целевая ситуация
    if current_situation.is_solved():
        return path

    for action in range(current_situation.n):
        next_situation = make_move(current_situation, action)

        if not next_situation or next_situation in stack:
            continue

        # Если новая ситуация валидна
        if next_situation:
            result = search_depth(next_situation, path + [action], stack + [next_situation])    
            if result:
                return result

    return None  # Решение не найдено
