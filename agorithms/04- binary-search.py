def binarySearch(arr, item, left=0, right=None):
    if right is None:
        right = len(arr)

    if left == right:
        return False

    mid = int((left + right)/2)

    if arr[mid] == item:
        return mid
    elif arr[mid] < item:
        return binarySearch(arr, item, mid + 1, right)
    elif arr[mid] > item:
        return binarySearch(arr, item, left, mid)


print(binarySearch([1, 1, 5, 7], 5))
