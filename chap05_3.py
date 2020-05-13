"""주석
    꼼수"""
# a, b = 10, 20

# print("# 교환 전")
# print("a:", a)
# print("b:", b)
# print()

# a, b = b, a

# print("# 교환 후")
# print("a:", a)
# print("b:", b)
# print()


# def test_func():
#     return (10, 20)

# c, d = test_func()
# print("c:", c, "d:", d)


# def call_10_times(func):
#     for i in range(10):
#         func()

# def print_hello():
#     print("Hello")

# call_10_times(print_hello)


# def power(item):
#     return item * item

# def under_3(item):
#     return item < 3

# power = lambda item: item * item
# under_3 = lambda item: item < 3

list_input = [1, 2, 3, 4, 5]

output = map(lambda item: item * item, list_input)
print("# map() 함수의 실행결과")
print("map(power, list_input):", output)
print("map(power, list_input):", list(output))

output = filter(lambda item: item < 3, list_input)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input):", output)
print("filter(under_3, list_input):", list(output))

