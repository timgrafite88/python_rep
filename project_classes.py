
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'{super().__str__()}\nСредняя оценка за лекции: {sum(self.grades) / len(self.grades):.1f}'

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
        return super().__str__()

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}'

# Создание экземпляров классов
student1 = Student('Ruoy', 'Eman', 'Male')
student2 = Student('Alice', 'Smith', 'Female')

lecturer1 = Lecturer('John', 'Doe')
lecturer2 = Lecturer('Jane', 'Doe')

reviewer1 = Reviewer('Mike', 'Johnson')
reviewer2 = Reviewer('Emily', 'Brown')

# Пример использования методов
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 7)

student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 8)

# Функции для подсчета средней оценки
def avg_grade_students(students, course):
    grades_sum = sum([sum(student.grades.get(course, [])) for student in students])
    grades_count = sum([len(student.grades.get(course, [])) for student in students])
    return grades_sum / grades_count if grades_count != 0 else 0

def avg_grade_lecturers(lecturers, course):
    grades_sum = sum([sum(lecturer.grades.get(course, [])) for lecturer in lecturers])
    grades_count = sum([len(lecturer.grades.get(course, [])) for lecturer in lecturers])
    return grades_sum / grades_count if grades_count != 0 else 0

# Вызов функций для подсчета средней оценки за домашние задания и за лекции
avg_grade_students_result = avg_grade_students([student1, student2], 'Python')
avg_grade_lecturers_result = avg_grade_lecturers([lecturer1, lecturer2], 'Python')

print(f'Средняя оценка за домашние задания по курсу Python: {avg_grade_students_result:.1f}')
print(f'Средняя оценка за лекции по курсу Python: {avg_grade_lecturers_result:.1f}')