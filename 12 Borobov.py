class Friends:
    def __init__(self, connections):
        self.connections = []
        [self.connections.append(x) for x in connections if x not in self.connections]

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        if self.connections != []:
            result_set = self.connections[0]
            for element in self.connections:
                result_set = result_set.union(element)
            return result_set
        else:
            return {}

    def connected(self, name):
        result_set = set()
        for element in self.connections:
            if name in element:
                result_set = result_set.union(element)
        result_set.discard(name)
        return result_set


class Group:
    def __init__(self, group_name, course, members=None):
        if members is None:
            members = []
        self.group_name = group_name
        self.course = course
        self.members = members

    def add_member(self, group_member):
        self.members.append(group_member)

    def student_avg_mark(self):
        avg_dict = {}
        for member in self.members:
            avg_list = []
            for value in member.scores.values():
                avg_value = sum(value) / len(value)
                avg_list.append(avg_value)
            avg_score = sum(avg_list) / len(avg_list)
            avg_dict[member.name + member.second_name] = round(avg_score, 3)
        return avg_dict

    def group_avg_mark(self):
        student_avg_mark_list = self.student_avg_mark()
        avg_mark = 0
        for student_mark in student_avg_mark_list.values():
            avg_mark += student_mark
        return round(avg_mark / len(student_avg_mark_list), 3)

    def lesson_avg_mark(self, lesson_name):
        avg_mark = []

        for member in self.members:
            if lesson_name in member.scores:
                avg_mark.append(sum(member.scores[lesson_name]) / len(member.scores[lesson_name]))

        return round(sum(avg_mark) / len(avg_mark), 3)


class GroupMember:
    def __init__(self, name, second_name, patronymic, scores=None):  # scores format = {lesson: [marks]}
        if scores is None:
            scores = {}
        self.name = name
        self.second_name = second_name
        self.patronymic = patronymic
        self.scores = scores

    def add_lesson(self, lesson_name):
        self.scores[lesson_name] = []

    def del_lesson(self, lesson_name):
        del self.scores[lesson_name]

    def add_marks(self, lesson_name, marks):
        marks = [] + marks  # На случай если, будет добавлена одна оценка, мы ее обернем массив и потом добавим массив как ключ предмета в score
        if lesson_name not in self.scores:
            self.add_lesson(lesson_name)
        self.scores[lesson_name] = self.scores[lesson_name] + marks

dima = GroupMember('Dima', 'Borobov', 'Victorovoch')
dima.add_marks('Философия', [3,4,5,5,5])
dima.add_marks('Math', [2,2,1,3,5])
dima.add_marks('Eng', [4,4,4,4,5])

Jenya = GroupMember('Jenya', 'Korolev', 'Victorovoch')
Jenya .add_marks('Философия', [2,2,2,2,5])
Jenya .add_marks('Math', [5,4,4,4,3])
Jenya .add_marks('Eng', [2,1,4,4,3])

Nikita = GroupMember('Nikita', 'Nikitin', 'Victorovoch')
Nikita.add_marks('Философия', [2,3,3,4,5])
Nikita.add_marks('Math', [5,5,5,3,2])
Nikita.add_marks('Eng', [5,5,5,5,5])

group = Group('710-1', 'III')
group.add_member(dima)
group.add_member(Jenya)
group.add_member(Nikita)

print(dima.scores)
print(Jenya.scores)
print(Nikita.scores)

print(group.student_avg_mark())
print(group.group_avg_mark())
print(group.lesson_avg_mark('Философия'))
