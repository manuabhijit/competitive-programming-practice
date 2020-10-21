import math

a = {
    
}

def getSortedWindow(arrOld, new, delete):
    if new == delete:
        return arrOld
    arr = []
    isRemoved = False
    isAdded = False
    for e in arrOld:
        if new < e and isAdded is False:
            isAdded = True
            arr.append(new)

        if e == delete and isRemoved is False:
            isRemoved = True
        else:
            arr.append(e)
    if isAdded is False:
        isAdded = True
        arr.append(new)
    return arr


def findMedian(runningWindow, wlenght):
    if wlenght % 2 == 0:
        return (
            runningWindow[math.floor(wlenght/2)] +
            runningWindow[math.floor(wlenght/2 - 1)]
        )
    else:
        return runningWindow[math.floor(wlenght/2)]


def activityNotifications(expenditure, d):
    runningWindow = expenditure[0:d]
    runningWindow.sort()
    count = 0

    for i, e in enumerate(expenditure[d:]):
        newElm = e
        oldElm = expenditure[i]
        median = findMedian(runningWindow, d)
        runningWindow = getSortedWindow(runningWindow, newElm, oldElm)
        if newElm >= median * 2:
            count = count + 1
    return count


print(activityNotifications([1, 2, 3, 4, 4], 4))
