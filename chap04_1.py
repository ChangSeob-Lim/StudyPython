# array = [273, 32, 103, "문자열", True, False, 3.141592]
# print(array)

# array[0] = "리스트"
# print(array)
# print(array[3][1])

# array2 = [[1,2,3], [4,5,6], [7,8,9]]
# print(array2[2][1])

list_a = [11,42,53]
list_b = [45,57,68]

print("#리스트")
# print(list_a)
# print(list_b)
# print(list_a + list_b)

list_c = list_a + list_b
# print(list_c)
# print(list_b * 4)
# print(len(list_c))
# print(list_c[len(list_c) - 1])
# print(list_c[-len(list_c)])

list_a.append(77) # 마지막에 추가
list_a.append(99)
print(list_a)

list_a.insert(1, 34) # 원하는 위치에 추가
print(list_a)

list_a.extend([14,15,16]) # 여러개 입력 가능
print(list_a)

del list_a[1] # 제거
print(list_a)

list_a.pop(1)
print(list_a)

del list_a[:3]
print(list_a)

list_a.append(14)
list_a.remove(14) # 처음 나오는 숫자만 제거
print(list_a)

print("14 in ? {}".format(14 in list_a))
print("11 in ?", 11 in list_a)

list_a.clear()
print(list_a)

# for i in range(5):
#     print("{}번 출력".format(i + 1))

array = [273, 32, 103, 57, 52]

for item in array:
    print(item)