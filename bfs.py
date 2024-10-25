from collections import deque
from model import Situation
from make_move import make_move

def bfs(init):
    """
    Функция поиска в ширину (Breadth-First Search, BFS).

    Берётся начальное ситуация и строится дерево с помощью очереди,
    где каждый узел - это ситуация, а каждый ребро - это действие,
    которое привело к этому состоянию.

    Алгоритм работает следующим образом:
    1. Инициализируем очередь, содержащую начальное ситуация.
    2. Берём верхний элемент очереди, это текущее ситуация.
    3. Если текущее ситуация - это целевое, то возвращаем путь,
       который привёл к этому состоянию.
    4. Иначе, генерируем все возможные действия (0-3) и
       добавляем в очередь новые ситуации, полученные из текущего,
       с обновлённым путём.
    5. Если очередь пуста, то решение не найдено.

    :param initial_situation: начальное ситуация
    :return: путь, который привёл к целевому состоянию, или None,
             если решение не найдено
    """
    visited = set()  # Храним все посещённые ситуации
    queue = deque(
        [(init, [])]
    )  # Каждый элемент: (текущее ситуация, путь действий)

    while queue:
        current_situation, path = queue.popleft()
        #print(current_situation)
        #input()
        # Проверяем, достигнуто ли целевое ситуация
        if current_situation.is_solved():
            return path

        # Пропускаем, если это ситуация уже было посещено
        if current_situation in visited:
            continue

        # Добавляем текущее ситуация в посещённые
        visited.add(current_situation)

        # Генерируем все возможные действия (0-3)
        for action in range(4):
            next_situation = make_move(current_situation, action)

            # Если новое ситуация валидно и не посещено ранее
            if next_situation and next_situation.isValid(*next_situation.position) and next_situation not in visited:
                # Добавляем новое ситуация в очередь с обновлённым путём
                queue.append((next_situation, path + [action]))

    return None  # Решение не найдено