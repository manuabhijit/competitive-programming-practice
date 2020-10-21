a = [1, 5, 5, 25, 125]

leftMap = {}
rightMap = {}


def gpTupple(arr, k):
    count = 0
    for e in arr:
        leftMap[e] = 0
        if rightMap.get(e) is not None:
            rightMap[e] += 1
        else:
            rightMap[e] = 1

    for cMid in arr:
        if rightMap[cMid] >= 1:
            rightMap[cMid] -= 1
            cLeft = cMid/k
            cRight = cMid*k

            if isInt(cLeft) and isInt(cRight):
                cLeft = int(cLeft)
                cRight = int(cRight)

                if rightMap.get(cRight) is not None and leftMap.get(cLeft) is not None:
                    count += (rightMap[cRight] * leftMap[cLeft])
            leftMap[cMid] += 1

    return count


def isInt(n):
    return n - int(n) == 0


print(gpTupple(a, 5))
