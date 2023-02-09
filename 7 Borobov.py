import re

"""
#1 Task: Анализ текста. Популярность.
text = input('Введите текст: ')
chars_popularity = {}
words_popularity = {}
words_from_text = re.split(";|, |\.| ", text)
for letter in text:
    if not (letter in chars_popularity):
        chars_popularity[letter] = text.count(letter)
for word in words_from_text:
    if not (word in words_popularity):
        words_popularity[word] = text.count(word)
print(f'text = "{text}", результат:', end='')
print(f"""
#    chars_popularity = {chars_popularity};
#    words_popularity = {words_popularity}
#    """)
#Нужно убрать однострочные комментарии с трех строк снизу

"""#2 Task: Римские цифры  78 LXXVIII
numbers = {1: 'I', 2: 'II', 3:'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
           40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M',
} #I V X L C D M
number = int(input('Введите число, которое нужно перевести в римскую систему счисления: '))
number_copy = number
result_number = ''
while number_copy != 0:
    multiplier = 100 #вводим переменную для сравнения (число может повторяться максимум три раза)
    final_key = 0
    for key in numbers.keys():
        div_result = number_copy // key
        if multiplier >= div_result > 0:
            multiplier = div_result
            final_key = key
    result_number += numbers[final_key] * multiplier
    number_copy -= final_key * multiplier
print(f"x = {number}, результат: '{result_number}'")"""
"""#3 Task: Ленивый спекулянт
rates = {'Sberbank': 57.8, 'VTB24': 56, 'SovkomBank': 56.1, 'HalvaBank': 65.9, 'Dinkoff': 56} # Исходный словарь 'Sberbank': 57.8, 'VTB24': 56, 'SovkomBank': 56.1, 'HalvaBank': 65.9, 'Dinkoff': 56

if len(rates) == 0:
    print('Ошибка: Нет данных')
else:
    min_rate = min(rates.values())

bank_list = [key for key in rates.keys() if rates[key] == min_rate]

if len(bank_list) == 1:
    print(f'rates = {rates}, результат: {bank_list[0]} -> {min_rate}')
elif len(bank_list) >= 1:
    print('Банки предоставляющие самые выгодные условия: ', end='')
    print(*bank_list, sep=', ', end=', ')
    print(f'по курсу: {min_rate}')"""
"""#Task 4: Вверх дном
#Решая 3 задание, нашел способ выполнить это
book = {'Petr': '546810', 'Katya': '241815'}
reverse_book = dict(zip(book.values(), book.keys()))
print(f' book = {book}, результат: {reverse_book}')"""
"""#5 Task: Структурируем данные
dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]
dates_and_rates = dict(zip(dates, rates))
print(f"""#dates = {dates}, rates = {rates}, результат:
#        {dates_and_rates}
#     """)"""
#6 Junior-: Судья игры "Крестики-нолики"
data = [
    "XOOOX",
    "OXXOX",
    "XOXOO",
    "XOOXX",
    "XXXOX",
 ] #Только для квадратных матриц
check_X = 'X' * len(data)
check_O = 'O' * len(data)
print(check_O)
add_comb = ''
main_diagonal = ''
side_diagonal = ''
result = 'D'
#Создадим 8 комбинаций при которых кто то может выиграть
comb_list = data[:] #Скопируем матрицу (строки для горизонтальной проверки)
for i in range(len(data)):
    for j in range(len(data)):
        if i == j:
            main_diagonal += data[i][j] #Создаем строки для главной диагонали
        if i + j + 1 == len(data):
            side_diagonal += data[i][j] #Создаем строки для побочной диагонали
        add_comb += data[j][i] #Создаем строки для вертикальной проверки
    comb_list.append(add_comb)
    add_comb = ''
comb_list.append(main_diagonal)
comb_list.append(side_diagonal)
#Проверка на наличие выигрыша у Х или у О, иначе result изначально равна D
for comb in comb_list:
    if comb == check_X:
        result = 'X'
        break
    elif comb == check_O:
        result = 'O'
        break
print('data = [')
for row in data:
    print('{0:>8}'.format('"' + row + '"'), end=', \n')
print(f']  -> "{result}"')
