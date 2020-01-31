def fibonacci(limit):
    returnData = []
    a = 0
    b = 1

    returnData.append(a)
    returnData.append(b)

    for item in range(0, limit):
        c = a + b
        a = b
        b = c
        returnData.append(c)
    return returnData


print(fibonacci(100))
