# Задачи 3.6 Junior-
"""
#1 Task
name = input('Please enter your name: ')
surname = input('Please enter your surname: ')
print(f'Hello {name} {surname}! You just delved into Python. Great start!')
"""
"""
#2 Task
Я не смог с нуля сделать 2е задание, я посмотрел ответ и разобрал каждую строчку программы.
"""
"""
#3 Task
text = input('Please, put your text: ').title()
print(text)
"""

"""
#Task 4
amount = float(input('Enter amount: '))
print('{0:,}'.format(round(amount, 2)))
"""

"""
#Junior
#Task 5
width = int(input('Enter width: '))
length = width * 3
for w in range(length):
    if w == 0 or w == length-1:
        print('*' * length)
    else:
        print('*' + '-' * (length-2) + '*')
"""

"""
"""
#Junior+
#6 Task
number = int(input('Enter your number: '))
while number == 0:
    number = int(input('Enter your number: '))

first_number = number
digit = number % 10
solve = 1
while number != 0:
    if digit != 0:
        solve = solve * digit
        number = number // 10
        digit = number % 10
    else:
        number = number // 10
        digit = number % 10
print(f'{first_number} and result {solve}')

