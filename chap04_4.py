# numbers = [1,2,3,4,5,6]

# for i in reversed(numbers):
#     print("첫번째 반복문 {}".format(i))
# print()

# for i in reversed(numbers):
#     print("두번째 반복문 {}".format(i))


# example_list = ["item A", "item B", "item C", "item D"]

# print("# 단순 출력")
# print(example_list)
# print()

# print("# enumerate() 함수 적용 출력")
# print(enumerate(example_list))
# print()

# print("# list() 함수로 강제 변환 출력")
# print(list(enumerate(example_list)))
# print()

# print("# 반복문과 조합하기")
# for i, value in enumerate(example_list):
#     print("{}번째 요소는 {}입니다.".format(i, value))


# example_dict = {
#     "키A" : "값A",
#     "키B" : "값B",
#     "키C" : "값C",
#     "키D" : "값D"
# }

# print("# 딕셔너리의 item() 함수")
# print("item():", example_dict.items())
# print()

# for key, element in example_dict.items():
#     print("dictionary[{}] = {}".format(key, element))


array = []

for i in range(1, 20, 1):
    array.append(2 ** i)

print(list(array))
print()

array2 = [2 ** i for i in range(4, 20)]
print(array2)
print()

array3 = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array3 if fruit != "초콜릿"]

print(output)