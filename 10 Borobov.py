# 1 Task: Градусник

def cel_to_fahr(init_list):
    result_list = [1.8 * x + 32 for x in init_list]
    return result_list


print(cel_to_fahr([39.2, 36.5, 37.3, 37.8]))


# 2 Task: Длинномер

def get_length(init_list):
    return list(map(lambda x: len(x), init_list))


print(get_length(['Eghjklknb', 'RLKJHG', 'Tom']))


# 3 Task: Рефакторинг
sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова', 'капитан']


def count_cap(sentence_list):
    new_list = [sentence for sentence in sentence_list if 'капитан' in sentence]
    return len(new_list)


print(count_cap(sentences))


# 4 Task: Возведение в степень
x = [2, 3, 4]
y = [10, 11, 12]


def x_pow_y(x, y):
    result_list = [a ** b for a, b in zip(x, y)]
    return result_list


print(x_pow_y(x, y))


# 5 Task: Ленивая функция

def lazy_func(n: int):
    for i in range(n + 1):
        if i == 0:
            yield -10
        elif i % 3:
            yield 45
        elif i % 5:
            yield i / 5 + 93
        else:
            yield i / 2


print(list(lazy_func(4)))


# 6 Task: Самый большой прямоугольник
"""
Идея следующая: от каждого столбца начинается поиск прилегающих столбцов не меньше текущего в обе стороны, соблюдая границы
"""

def largest_rect(value_list: list) -> int:
    left_idx = -1  # Левая граница
    right_idx = len(value_list)  # Правая граница
    cur_idx = 0  # Текущий индекс элемента
    sizes_list = []  # Список, где будут храниться значения всех возможных прямоугольников

    while cur_idx != right_idx:
        column_counter = 1
        r_pointer = cur_idx + 1
        l_pointer = cur_idx - 1
        check_right = True
        check_left = True
        check_both = True

        if value_list[cur_idx] == 0:
            left_idx = cur_idx
            cur_idx += 1
            continue

        while check_both:
            if r_pointer < right_idx and value_list[r_pointer] >= value_list[cur_idx]:
                column_counter += 1
                r_pointer += 1
            else:
                check_right = False

            if l_pointer > left_idx and value_list[l_pointer] >= value_list[cur_idx]:
                column_counter += 1
                l_pointer -= 1
            else:
                check_left = False

            check_both = check_left + check_right

        sizes_list.append(value_list[cur_idx] * column_counter)
        cur_idx += 1
    return max(sizes_list)


print(largest_rect([2, 1, 4, 5, 1, 12, 3]))
print(largest_rect([5]))  # 5
print(largest_rect([5, 3]))  # 6
print(largest_rect([1, 1, 4, 1]))  # 4
print(largest_rect([1, 1, 3, 1]))  # 4
print(largest_rect([2, 1, 4, 5, 1, 3, 3]))  # 8
