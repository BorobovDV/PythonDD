from math import sqrt

# 1 Task: Не уникальные элементы.
numbers = [10, 9, 10, 10, 9, 8]
not_unique_numbers = [x for x in numbers if numbers.count(x) > 1]
print(f'{numbers}, результат: {not_unique_numbers}')

# 2 Task: Перестановки.
x, y, z, n = 1, 1, 1, 2
result = [[ix, iy, iz] for ix in range(x + 1)
          for iy in range(y + 1)
          for iz in range(z + 1)
          if (ix + iy + iz) != n
          ]
"""for ix in range(x + 1):
    for iy in range(y + 1):
        for iz in range(z + 1):
            if (ix + iy + iz) != n:
                result.append([ix, iy, iz])"""
print(result)

# 3 Task: Удвоенные нечетные.
n = 10
result_list = [i * 2 for i in range(n) if i % 2]
print(f'n = {n}, результат: {result_list}')

# 4 Junior: Дешифратор.


def rotation_on_90_degrees(grid_matrix):
    length = len(grid_matrix)
    row = ''
    rotate_list = []
    for j in range(length):
        for i in range(length - 1, -1, -1):
            row += grid_matrix[i][j]
        rotate_list.append(row)
        row = ''
    return rotate_list


def decoder(grid_matrix, password_matrix):
    length_grid = len(grid_matrix)
    result_word = ''
    for i in range(length_grid):
        for j in range(length_grid):
            if grid_matrix[i][j] == 'X':
                result_word += password_matrix[i][j]
    return result_word


grid = [
        '....',
        'X..X',
        '.X..',
        '...X'
]
grid_copy = grid.copy()
password = [
        'xhwc',
        'rsqx',
        'xqzz',
        'fyzr'
]
decrypt_word = ''
for i in range(4):
    decrypt_word += decoder(grid_copy, password)
    grid_copy = rotation_on_90_degrees(grid_copy)

print(decrypt_word)

# 5 Task: Возраст привидений
def isFibonacci(number):
    check_state_one = sqrt(5 * (number ** 2) + 4) % 1
    check_state_two = sqrt(
        abs(5 * (number ** 2) - 4)) % 1  # abs() добавил, чтобы на проверке 0 параметры sqrt не уходили в минус

    if check_state_one == 0 or check_state_two == 0:
        return True
    else:
        return False


default_transparency = 10000
transparency_and_ages_dict = {}
for i in range(5001):
    if isFibonacci(i):
        transparency_and_ages_dict[default_transparency - i] = i
        default_transparency -= i
    else:
        default_transparency += 1
        transparency_and_ages_dict[default_transparency] = i

transparency = 9977  # Ввод прозрачности
if transparency in transparency_and_ages_dict:
    print(f'прозрачность = {transparency}, возраст: {transparency_and_ages_dict[transparency]}')
else:
    print(f'Прозрачность равная: {transparency}, является переходной')
