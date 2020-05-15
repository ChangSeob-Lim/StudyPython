class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg())

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

# std_a = Student("윤인성", 88, 87, 95, 88)
# std_b = Student("구지연", 88, 87, 95, 100)
# print("std의 클래스 인스턴스 여부:", isinstance(std, Student))

# print("이름", "총점", "평균", sep='\t')
# print(str(std_a))
# print(str(std_b))

# print(std_a < std_b)

students = [
    Student("a", 11, 12, 13, 14),
    Student("b", 25, 26, 27, 28),
    Student("c", 39, 30, 43, 43),
    Student("d", 46, 47, 48, 49),
    Student("e", 59, 85, 65, 95),
    Student("f", 16, 56, 67, 86)
]

print("학생수 :", Student.count)
print("이름", "총점", "평균", sep='\t')
for student in students:
    print(str(student))

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        self.__radius = value

c = Circle(1)

c.set_radius(5)
# print(c.get_radius()) # @property 없을때
print(c.get_radius) # @property 있을때