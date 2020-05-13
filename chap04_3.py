# for i in range(5):
#     print(i, " = 반복변수")
# print()

# for i in range(5, 10):
#     print(i, "= 반복변수")
# print()

# for i in range(0, 10, 3):
#     print(i, "= 반복변수")
# print()

# array = [11, 22, 33, 44, 55, 66]

# for i in range(len(array)):
#     print("{}번째 반복: {}".format(i + 1, array[i]))
# print()

# for i in reverse(range(5)): #range(5, -1, -1):
#     print(i)
# print()

# while True:
#     print(".", end="")

# i = 0
# while True:
#     print("{}번째 반복입니다.".format(i))
#     i += 1
#     input_text = input("> 종료하시겠습니까? (y): ")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break

numbers = [5, 15, 6, 20, 7, 25]

for num in numbers:
    if num < 10:
        continue

    print(num)
