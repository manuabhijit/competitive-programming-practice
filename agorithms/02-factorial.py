def factorial(num):
    return 1 if num <= 0 else factorial(num-1) * num


print(factorial(300))
