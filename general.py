#!/bin/python3
import math
import os
import random

# Common Typed Variables
true = True
false = False
none = None
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


# END OF MY ACTUAL CODE
# PADDING
# PADDING
# PADDING
# PADDING
# EOF
