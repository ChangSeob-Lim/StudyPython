class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def toString(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg())


# student = Student()

students = [
    Student("a", 11, 12, 13, 14),
    Student("b", 25, 26, 27, 28),
    Student("c", 39, 30, 43, 43),
    Student("d", 46, 47, 48, 49),
    Student("e", 59, 85, 65, 95),
    Student("f", 16, 56, 67, 86)
]

print("이름", "총점", "평균", sep='\t')
for student in students:
    print(student.toString())