import re #Для решения задачи #5 Junior+
# Задачи 6.6 Junior-
"""
#1 Task: Последний с четными
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_sum = 0
n = len(elements)
for i in range(n):
    if i % 2 == 0:
        evens_sum += elements[i]
if n != 0:
    print(f'elements = {elements} , результат: {evens_sum * elements[n - 1]}')
else:
    print(f'elements = {elements} , результат: {0}')
"""
"""
#2 Task: Max-min
elements = []
if len(elements) == 0:
    print(f'elements = {elements} , результат: {0}')
else:
    print(f'elements = {elements} , результат: {round((max(elements) - min(elements)), 3)}')
"""
"""
#3 Task: Умная сортировка
elements = (-1, -2, -3, 0)
elements_copy = elements
print(f'elements = {elements}, результат: {sorted(elements_copy, key=abs)}')
"""
"""
#4 Задача Junior
elements = [-1, 2, 3, 20, -20, 24, 43]
middle = len(elements) // 2
mediana = 0
sorted_elements = sorted(elements)
if len(elements) % 2 == 0:
    mediana = (sorted_elements[middle] + sorted_elements[middle - 1]) / 2
else:
    mediana = sorted_elements[middle]
print(f'elements = {elements}, результат: {mediana}')
"""
"""
#5 Junior+
#Метод, метод который возвращает True, если все буквы letters есть в слове word
def check_letters(letters, text):
    success = True
    for letter in letters:
        if not (letter in text):
            success = False
            break
    return success


vowels = 'AEIOUY'
consonants = 'BCDFGHJKLMNPQRSTVWXZ'
text = input('Пожалуйста введите ваш текст: ')
text_list = re.split(";|,|\.| ", text)
word_counter = 0
for word in text_list:
    #Перевели слово в верхний регистр для дальнейшего удобства
    upper_word = word.upper()
    if len(upper_word) > 1 and word.isalpha():
        #Создаем списки с буквами под четными и нечетными буквами
        even_letters = [upper_word[i] for i in range(0, len(upper_word), 2)]
        odd_letters = [upper_word[i] for i in range(1, len(upper_word), 2)]
        #Проверяем условие "полосатости"
        if check_letters(even_letters, vowels) and check_letters(odd_letters, consonants) or check_letters(even_letters, consonants) and check_letters(odd_letters, vowels):
            word_counter += 1
print(f'text = "{text}", результат: {word_counter}')"""

