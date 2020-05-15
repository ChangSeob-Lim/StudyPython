# students = [
#     { "이름":"홍길동", "score":87 },
#     { "이름":"홍길순", "score":90 },
#     { "이름":"홍길자", "score":100 },
#     { "이름":"홍길국", "score":60 },
#     { "이름":"홍길숙", "score":0 }
# ]

# for student in students:
#     print("이름: {}, 점수: {}".format(student.get("이름"), student.get("score")))

def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student.get("korean") + student.get("math") + \
        student.get("english") + student.get("science")

def student_get_avg(student):
    return student_get_sum(student) / 4

def student_toString(student):
    return "{}\t{}\t{}".format(
        student.get("name"),
        student_get_sum(student),
            student_get_avg(student))

students = [
    create_student("a", 11, 12, 13, 14),
    create_student("b", 25, 26, 27, 28),
    create_student("c", 39, 30, 43, 43),
    create_student("d", 46, 47, 48, 49),
    create_student("e", 59, 85, 65, 95),
    create_student("f", 16, 56, 67, 86)
]
students.append(create_student("g", 77, 77, 77, 77))

# print(students)

print("이름", "총점", "평균", sep='\t')
for student in students:
    print(student_toString(student))
