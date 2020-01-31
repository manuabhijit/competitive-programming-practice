def palindrome(num):
    num1 = num
    num2 = 0
    while num != 0:
        digit = (num % 10)
        num2 = num2 * 10 + (num % 10)
        num = (num - digit)/10

    return num1 == num2
