# numbers = [1,2,3,4,5,6]

# for i in reversed(numbers):
#     print("첫번째 반복문 {}".format(i))
# print()

# for i in reversed(numbers):
#     print("두번째 반복문 {}".format(i))
# print()

example_list = ["item A", "item B", "item C", "item D"]

print("# 단순 출력")
print(example_list)
print()

print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))
print()

example_dict = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
    "키D" : "값D"
}

print("# 딕셔너리의 item() 함수")
print("item():", example_dict.items())
print()

for key, element in example_dict.items():
    print("dictionary[{}] = {}".format(key, element))