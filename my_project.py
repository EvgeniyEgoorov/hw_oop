class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        for values in self.grades.values():
            return round(sum(values) / len(values), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Пожалуйста, укажите имя студента')
            return
        return self.avg_rate() < other.avg_rate()

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.avg_rate()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Student.avg_rate(self)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Пожалуйста, укажите имя лектора')
            return
        return Student.avg_rate(self) < Student.avg_rate(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_student = Student('Tom', 'Jones', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

other_student = Student('Peter', 'Hunt', 'your_gender')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['JS']

some_lecturer = Lecturer('Jake', 'Smith')
some_lecturer.courses_attached += ['JS']

other_lecturer = Lecturer('Jo', 'Black')
other_lecturer.courses_attached += ['Python']
other_lecturer.courses_attached += ['JS']

some_reviewer = Reviewer('Billy', 'Baxter')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 6)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_reviewer.rate_hw(other_student, 'Python', 4)
some_reviewer.rate_hw(other_student, 'Python', 5)
some_reviewer.rate_hw(other_student, 'Python', 8)

other_student.rate_lecture(some_lecturer, 'JS', 7)
other_student.rate_lecture(some_lecturer, 'JS', 9)
other_student.rate_lecture(some_lecturer, 'JS', 10)

other_student.rate_lecture(other_lecturer, 'JS', 5)
other_student.rate_lecture(other_lecturer, 'JS', 7)
other_student.rate_lecture(other_lecturer, 'JS', 9)

#
print(f'Оценки студентов: {some_student.grades}', '\n')
print(f'Оценки преподавателей: {some_lecturer.grades}', '\n')

print(some_reviewer, '\n')
print(some_lecturer, '\n')
print(some_student, '\n')

print(some_student < other_student)
print(some_lecturer > other_lecturer)
