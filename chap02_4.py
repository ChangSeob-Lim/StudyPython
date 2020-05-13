# format_a = "{}".format(10000)
# format_b = "{} {}".format(10, 20)
# format_c = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
# format_d = "{} {}{}".format(1, "문자열", True)

# print(format_a)
# print(format_b)
# print(type(format_b))
# print(format_c)
# print(format_d)
# print(type(format_d))


# output_a = "{:+010d}".format(-30)
# output_b = "{:+010f}".format(3.141592)
# Pi = 3.141592
# output_c = "{:g}".format(52.01234560000)

# print(output_a)
# print(output_b)
# print(output_c)


# input_s = "Hello Python Programing!!"
# input_t = """
#      안녕하세요     
# 테스트 입니다.     
# """

# print(input_s.upper()) #대문자로 바꿈
# print(input_s.lower()) #소문자로 바꿈
# print(input_t.strip()) #문자열 양옆의 공백을 제거 lstrip, rstrip


# check_str = "TrainA10"
# print(check_str.isalnum())
# check_str = "TrainA10"
# print(check_str.isalpha())
# print("하세" in "안녕하세요")


a = "10,20,30,40,50,60".split(",") #문자열을 특정한 문자로 자름
print(a) #결과는 리스트로 출력