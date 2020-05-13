import time

counter = 0

dictionary = {
    1 : 1,
    2 : 1
}

def factorial(n):
    # output = 1

    # for i in range(1, n + 1):
    #     output *= i

    # return output

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print("1! :", factorial(1))
# print("2! :", factorial(2))
# print("3! :", factorial(3))
# print("4! :", factorial(4))
# print("5! :", factorial(5))
# print("100! : {}".format(format(factorial(100), ',d')))

def fibonacci(n):
    global counter
    counter += 1

    # if n == 1 or n == 2:
    #     return 1
    # else:
    #     return fibonacci(n-1) + fibonacci(n-2)

    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

print("fibonacci(1) :", fibonacci(1))
print("fibonacci(2) :", fibonacci(2))
print("fibonacci(3) :", fibonacci(3))
print("fibonacci(4) :", fibonacci(4))
print("fibonacci(5) :", fibonacci(5))
print("fibonacci(30) : {}".format(format(fibonacci(30), ',d')))

# start = time.time()
# print("fibonacci(35) : {} / counter : {} / time : {}".format(fibonacci(35), counter, time.time() - start))
# print(dictionary)
# print("dict_size {}".format(len(dictionary)))