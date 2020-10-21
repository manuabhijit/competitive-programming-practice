import math


def minTime(machines, goal):
    return binary(machines, goal, 0, 10)


def binary(machines, goal, left, right):
    mid = math.floor((left + right)/2)
    if left == mid or right == mid:
        return mid

    check = checkAchieved(machines, goal, mid)
    if check is False:
        return binary(machines, goal, mid, right)
    else:
        check2 = checkAchieved(machines, goal, mid - 1)
        if check2 is False:
            return mid
        else:
            return binary(machines, goal, left, mid)


def checkAchieved(machines, goal, day):
    achieved = 0
    for machine in machines:
        achieved = achieved + math.floor(day/machine)
        if achieved >= goal:
            return day
    return False


print(minTime([2, 3], 5))
