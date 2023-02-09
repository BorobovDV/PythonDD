# Задачи 5.6 Junior-

"""
#1 Task: Fizz Buzz
x = int(input('Введите число: '))
if (x % 3 == 0) and (x % 5 == 0):
    result = "Fizz Buzz"
elif x % 3 == 0:
    result = "Fizz"
elif x % 5 == 0:
    result = "Buzz"
else:
    result = x
print(f'x = {x}, результат: "{result}"')
"""

"""
#2 Task: Оценка числа
x = int(input('Введите число: '))
not_bad = [i for i in range(2, 6)]
not_good = [i for i in range(6, 21)]
if not(x % 2 == 0):
    print(f'x = {x}, результат: "Плохо"')
elif x in not_bad:
    print(f'x = {x}, результат: "Неплохо"')
elif x in not_good:
    print(f'x = {x}, результат: "Так себе"')
elif (x > 20):
    print(f'x = {x}, результат: "Отлично"')
else:
    print("Вы ввели число не удовлетворяющее требованиям программы.")
"""
"""
#3 Task: Последовательность
number = int(input('Введите число: '))
result = ''
if (number == 1):
    print(f'N = {number}, результат: 1')
else:
    for i in range(1, number + 1):
        result += str(i)
print(f'N = {number}, результат: {result}')
"""
"""
#4 Task: Секретное сообщение
text = input('Введите ваш текст: ')
text_list = text.split()
result = ''
for word in text_list:
    if word.istitle():
        result += word[0]
print(f'текст = "{text}"'
      f', если мы соберем все заглавные буквы, то получим сообщение "{result}".')
"""
#Задача 5.6 Junior
"""
text = input('Введите текст: ')
text_list = text.split()
result = False
count_of_word = 0
for i in range(len(text_list)):
    if not(text_list[i].isdigit()):
        count_of_word += 1
    else:
        count_of_word = 0
    if count_of_word >= 3:
        result = True
        break
print(f'text = "{text}", результат: {result}')
"""
#Задача 5.6О Junior+
"""
text_list = ["enough", "jokes"]
default_list = text_list.copy()
for i in range(len(text_list)):
    text_list[i] = text_list[i].replace("right", "left")
print(f'{default_list}, результат: "', end='')
print(*text_list, sep=',', end='')
print('"')
"""

