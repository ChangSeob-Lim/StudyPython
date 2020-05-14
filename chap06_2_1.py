try:
    number = int(input("정수 입력 > "))

    if number > 0:
        raise NotImplementedError("0보다 큼: 구현 안됨")
    else:
        raise NotImplementedError("0보다 작음: 구현 안됨")
except NotImplementedError as ex:
    print("NotImplementedError: 구현 하세요")
    print(ex)
except ValueError as ex:
    print("ValueError: 정수를 입력하세요")
except Exception as ex:
    print(type(ex))
    print(ex)
finally:
    print("종료")