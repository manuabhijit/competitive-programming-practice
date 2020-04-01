# Given an unsorted array A of size N of non-negative integers,
# find a continuous sub-array which adds to a given number S.

# Input:
# The first line of input contains an integer T
# denoting the number of test cases.
# Then T test cases follow. Each test case consists of two lines.
# The first line of each test case is N and S,
# where N is the size of array and S is the sum.
# The second line of each test case contains N space separated
# integers denoting the array elements.

# Output:
# For each testcase, in a new line,
# print the starting and ending positions(1 indexing) of first such
# occuring subarray from the left if sum equals to subarray, else print -1.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= Ai <= 1010

# Example:
# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10
# Output:
# 2 4
# 1 5

# Explanation :
# Testcase1: sum of elements from 2nd position to 4th position is 12
# Testcase2: sum of elements from 1st position to 5th position is 15

# !/bin/python3

import math
import os
import random

# Common Typed Variables
true = True
false = False
mone = None
lenght = len

# Common Indexing Variables
index = 0
i, j, k = (0, 0, 0)
summation = 0
product = 1

# Common Usage Blank Variables
arr = []
strr = ""
str_list = []
dictionary = {}

# Common Usage Variables
sqrt_2 = math.sqrt(2)
arr_100 = list(range(1, 100))
arr_revesed_100 = sorted(arr_100)
arr_random_100 = random.randint(1, 100)

# Constants
PI = 22/7
pi = round(PI, 2)

# Input streams
newLine = ""

# Input Reader 1


def inputReader_1():
    print("a")


def outputWriter_2(result, outputPath="output.txt"):
    global outputWriter_2_execution_counter

    try:
        outputWriter_2_execution_counter
    except Exception:
        outputWriter_2_execution_counter = true

    if outputWriter_2_execution_counter == true:
        outputWriter_2_execution_counter = false
    else:
        raise ValueError('A very specific bad thing happened.')

    if(outputPath is None):
        print(result)
    else:
        outputPath = os.environ['OUTPUT_PATH'] \
          if "OUTPUT_PATH" in os.environ else outputPath
        filePtr = open(outputPath, 'w')
        filePtr.write(str(result) + '\n')
        filePtr.close()


def readLine(dt=int):
    return input().strip() if dt == str else int(input().strip())


def readLineMap(dt=int, sep=''):
    return input().split() if dt == str else map(dt, input().split())


def readLineArray(dt=int, sep=''):
    return input().split() if dt == str else list(map(dt, input().split()))

# MY ACTUAL CODE


tc = readLine()

for _ in range(0, tc):
    l, s = readLineMap()
    arr = readLineArray()

    i, summ, f = (0, 0, False)
    for ind, el in enumerate(arr):
        summ = summ + el
        if summ == s:
            f = True
            print(i+1, ind+1)
            break
        elif summ > s:
            for _ in range(i, ind):
                summ = summ - arr[i]
                i = i + 1
                if summ <= s:
                    break
            if summ == s:
                print(i+1, ind+1)
                f = True
                break

    if f is not True:
        print('-1')

# END OF MY ACTUAL CODE
#
#
#
# EOF
