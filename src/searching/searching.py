def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    arr.sort()
    middle = len(arr) // 2
    pointer = middle
    if len(arr) < 1:
        return -1
    while arr[0] != target and middle > 0:
        if arr[middle] > target:
            arr = arr[:middle]
            middle = len(arr) // 2
            pointer -= middle + 1
        elif arr[middle] < target:
            arr = arr[middle+1:]
            middle = len(arr) // 2
            pointer += middle + 1
        else:
            arr[0] = arr[middle]
    if arr[0] == target:
        return pointer
    return -1  # not found
