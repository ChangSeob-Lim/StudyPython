# try except 연습

# try:
#     number_input = int(input("정수 입력 > "))

#     print("원의 반지름 :", number_input)
#     print("원의 둘레 :", 2 * 3.141592 * number_input)
#     print("원의 넓이 :", 3.141592 * number_input * number_input)
# except Exception as e:
#     print(type(e))
#     print(e)
#    print("뭔가 잘못 되었습니다.")
# else:
#     print("에러가 발생하지 않았습니다.")
# finally:
#     print("프로그램 종료")


# lists = ['11', '22', '33', '44', '하이', '55']
# outputs = []

# for item in lists:
#     try:
#         float(item)
#         outputs.append(item)
#     except:
#         pass
        
# print(outputs)


# f = open("./data/basic.txt", "r")
# try:
#     f.write("TEST!!")
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# print("file close? :", f.closed)


# def test():
#     print("test() start")
#     try:
#         print("test() try")
#         return
#         print("test() after return")
#     except:
#         print("test() except")
#     else:
#         print("test() else")
#     finally:
#         print("test() finally")

#     print("test() end")

# test()


lists = [52, 273, 32, 72, 100]

try:
    inputs = int(input("정수 입력 > "))
    print("{}번째 요소값 : {}".format(inputs, lists[inputs]))
    #error()
except ValueError as e:
    print("valueError")
    print(e)
except IndexError as e:
    print("IndexError")
    print(e)
except Exception as e:
    print("Exception")
    print(type(e))
    print(e)