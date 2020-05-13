# def print_3_times():
#     print("안녕하세요\n" * 3)

# def print_n_times(value, n):
#     for i in range(n):
#         print(value, end=" ")

# def print_n_times(value):
#     for i in range(10):
#         print(value, end=" ")

# def print_n_times(n=3, *values):
#     for i in range(n):
#         for value in values:
#             print(value, end=" ")
#         print()

# def print_n_times(*values, n = 3):
#     for i in range(n):
#         for value in values:
#             print(value, end=" ")
#         print()

# print_3_times()
# print_n_times("Hello", 4)
# print_n_times(n=4, "안녕하세요", "즐거운", "파이썬", "프로그래밍")
# print_n_times("안녕하세요", "즐거운", "파이썬", "프로그래밍", n=4)


# def func(a, b=10, c=20):
#     print(a + b + c)

# func(c=100, a= 50, b=50)


# def return_test():
#     return 100

# value = return_test()

# if(value == None):
#     print("value 값이 없음")
# else:
#     print("value = {}".format(value))


def multi_all(start, end):
    output = 1
    
    for i in range(start, end + 1):
        output *= i

    return output

print ("1 to 5 :", multi_all(1, 5))
print ("1 to 10 :", multi_all(1, 10))
print ("2 to 8 :", multi_all(2, 8))