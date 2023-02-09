# 1 Task: Список из числа
from numpy import mean


def reverse_list_of_number(n):
    str_n = str(n)
    n_list = list(str_n)
    n_list.reverse()
    return n_list


# 2 Task: Палиндром
def isPalindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False


# 3 Task: Деканат
students_list = [{'Surname': 'Боробов', 'Name': 'Дмитрий', 'Patronymic': 'Викторович', 'Birth_date': 2002, 'Course': 3, 'Group': '711-1', 'Scores': {'Физика': 5, 'ОБЖ': 4, 'Литература': 4, 'Математика': 5, 'География': 4}},
                 {'Surname': 'Ауров', 'Name': 'Анатолий', 'Patronymic': 'Кириллович', 'Birth_date': 2001, 'Course': 4, 'Group': '710-1', 'Scores': {'Физика': 4, 'Электроника': 3, 'Литература': 4, 'Математика': 5, 'Философия': 4}},
                 {'Surname': 'Редька', 'Name': 'Ян', 'Patronymic': 'Андреевич', 'Birth_date': 2004, 'Course': 1, 'Group': '710-2', 'Scores': {'Физика': 1, 'ОБЖ': 4, 'Литература': 4, 'Математика': 5, 'География': 5}},
                 {'Surname': 'Рыков', 'Name': 'Ян', 'Patronymic': 'Андреевич', 'Birth_date': 2004, 'Course': 2, 'Group': '722-1', 'Scores': {'Физика': 1, 'ОБЖ': 4, 'Литература': 4, 'Математика': 5, 'География': 5}},
                 {'Surname': 'Аленький', 'Name': 'Ян', 'Patronymic': 'Андреевич', 'Birth_date': 2004, 'Course': 3, 'Group': '722-1', 'Scores': {'Физика': 1, 'ОБЖ': 4, 'Литература': 4, 'Математика': 5, 'География': 5}},
                 {'Surname': 'Орлов', 'Name': 'Ян', 'Patronymic': 'Андреевич', 'Birth_date': 2004, 'Course': 4, 'Group': '710-1', 'Scores': {'Физика': 4, 'Электроника': 4, 'Литература': 4, 'Математика': 4, 'Философия': 4}},
                 {'Surname': 'Попов', 'Name': 'Ян', 'Patronymic': 'Андреевич', 'Birth_date': 2004, 'Course': 4, 'Group': '710-1', 'Scores': {'Физика': 2, 'Электроника': 3, 'Литература': 5, 'Математика': 2, 'Философия': 5}},
                 {'Surname': 'Ярый', 'Name': 'Ян', 'Patronymic': 'Андреевич', 'Birth_date': 2004, 'Course': 1, 'Group': '721-1', 'Scores': {'Матанализ': 5, 'ОИБ': 4, 'ПОПД': 5, 'ТИМП': 4, 'ЗИС': 4}},
                 {'Surname': 'Алан', 'Name': 'Ян', 'Patronymic': 'Андреевич', 'Birth_date': 2004, 'Course': 2, 'Group': '721-1', 'Scores': {'Матанализ': 4, 'ОИБ': 4, 'ПОПД': 5, 'ТИМП': 3, 'ЗИС': 4}},
                 {'Surname': 'Крылов', 'Name': 'Ян', 'Patronymic': 'Андреевич', 'Birth_date': 2000, 'Course': 5, 'Group': '034-1', 'Scores': {'Русский язык': 4, 'Экономика': 4, 'Физика': 4, 'Математика': 4, 'История': 4}},
                 {'Surname': 'Баснин', 'Name': 'Виктор', 'Patronymic': 'Валентинович', 'Birth_date': 2000, 'Course': 5, 'Group': '034-1', 'Scores': {'Русский язык': 4, 'Экономика': 4, 'Физика': 4, 'Математика': 4, 'История': 4}},
                 {'Surname': 'Быков', 'Name': 'Илья', 'Patronymic': 'Александрович', 'Birth_date': 2002, 'Course': 3, 'Group': '711-1', 'Scores': {'Физика': 3, 'ОБЖ': 3, 'Литература': 3, 'Математика': 3, 'География': 3}},

]



def course_student_list(list_of_students):
    alphabet_sorted = sorted(list_of_students, key=lambda x: (x['Course'], x['Surname']))
    return alphabet_sorted


def group_avg_lesson(list_of_student):
    group_set = {x['Group'] for x in list_of_student}
    group_list = sorted(list(group_set))
    result_list = []
    for group in group_list:
        scores_dict = {}
        count = 0
        for line in list_of_student:
            if group == line['Group']:
                if count == 0:
                    scores_dict = line['Scores']
                else:
                    mark_list = list(line['Scores'].values())
                    for lesson in list(scores_dict.keys()):
                        scores_dict[lesson] += mark_list[0]
                        mark_list.pop(0)
                count += 1
        for lesson, mark in scores_dict.items():
            scores_dict[lesson] = round(mark / count, 2)
        result_list.append({group: scores_dict})
    return result_list


def get_young_and_old(list_of_students):
    result_list = []
    sorted_students_list = sorted(list_of_students, key=lambda x: x['Birth_date'], reverse=True)
    result_list.append(sorted_students_list[0])
    result_list.append(sorted_students_list[len(sorted_students_list) - 1])
    return result_list


def best_student(list_of_student):
    group_set = {x['Group'] for x in list_of_student}
    group_list = sorted(list(group_set))
    copy_list = list_of_student[:]
    copy_list = sorted(copy_list, key=lambda x: x['Surname'])
    result_list = []
    for group in group_list:
        best_name = ''
        best_mark = -1
        for line in copy_list:
            if group == line['Group']:
                cur_name = line['Surname'] + ' ' + line['Name'] + ' ' + line['Patronymic']
                cur_mark = mean(list(line['Scores'].values()))
                if cur_mark > best_mark:
                    best_mark = cur_mark
                    best_name = cur_name
                copy_list.remove(line)
        result_list.append({group: {best_name: best_mark}})
    return result_list


"""list_std = best_student(students_list)
for x in list_std:
    print(x)"""


# Junior-: Пешки
""" Идея следующая: есть множество координат пешек, будем брать каждую и для нее находить координаты пешек, обеспечивающие безопасность проверяемой.
    Далее, получив координаты безопасных пешек, проверим есть ли они в нашем исходном множестве. """


def safe_point(any_set):
    counter = 0
    for coord in any_set:
        check_coord = []
        separated_coord = list(coord)  # Получаем массив, где 0ой элемент буква, 1ый - цифра
        if separated_coord[0] != 1:  # Т.е. не находится на 1ой горизонтали и может быть защищен
            separated_coord[1] = int(separated_coord[1]) - 1  # Уменьшаем значение горизонтали
            # изначально я хотел проверить случаи для крайних вертикалей (а и h), но потом понял, что можно этого не делать так как полученные
            # "безопасные" координаты физически не могут находиться на шахматной доске и проверку вхождения в исходный список не пройдут
            check_coord.append(chr(ord(separated_coord[0]) - 1) + str(separated_coord[1]))  # Добавление координаты диагонали слева
            check_coord.append(chr(ord(separated_coord[0]) + 1) + str(separated_coord[1]))  # Добавление координаты диагонали справа
            if check_coord[0] in any_set or check_coord[1] in any_set:
                counter += 1
    return counter


test_set = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
# print(safe_point(test_set))



