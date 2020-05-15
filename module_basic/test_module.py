PI = 3.14159265

# print("모듈 ")
# print(__name__)

def number_input():
    try:
        output = float(input("숫자 입력 > "))
        return output
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

def get_circumference(radius):
    return 2 * PI * radius

def get_circleArea(radius):
    return PI * (radius ** 2)

if __name__ == "__main__":
    print("get_circumference(10)", get_circumference(10))
    print("get_circleArea(10)", get_circleArea(10))