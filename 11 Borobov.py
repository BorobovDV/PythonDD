# 1 Task: Случайности не случайны
from random import uniform


def rand_is_not_rand(n: int):
    for i in range(n):
        yield uniform(0, n)


# 2 Task: Ленивое объединение
from itertools import chain


def lazy_union(x, y):
    return list(chain(x, y))

# 3 Task: Рефакторинг
def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids  # Ненужная проверка, т.к если список пуст, то item_ids is None даст False.
                                                         # Даже если придет [None], [None] is None все равно даст False и мы все равно назначим
                                                         # списку самого себя

    responses = []
    # При вызове responses_creator([1,3,2,5,6]) будет следующий вывод: [{'item_id': 1}, {'item_id': 3}, {'item_id': 2}, {'item_id': 5}, {'item_id': 6}]
    # Заменим цикл на генератор списка из словарей
    for item_id in item_ids:
        new_response = dict(item_id=item_id)
        responses.append(new_response)
    return responses


def responses_creator2(item_ids):
    return [{'item_id': x} for x in item_ids]

