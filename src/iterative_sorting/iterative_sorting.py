# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # TO-DO: swap
        # Your code here

    return arr


arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(bubble_sort(arr))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # create an array of 0s with len max+1
    # every time we see i, arr_0s[i] += 1
    # then create sorted_arr where each i in arr_0s is printed arr_0s[i] times

    arr_0s = [0 for _ in range(0, maximum + 1)]   #O(n) over maximum value
    for x in arr:  #O(n) over length of arr
        arr_0s[x] += 1
    sorted_arr = [x for x in range(maximum+1) if arr_0s[x] >= 1 for _ in range(arr_0s[x])] #O(n^2) ? over maximum value

    return sorted_arr
#so counting_sort might be more efficient for a long list of known small values (ratings from 1-4 or something)
#but less efficient for a list including large values
print(counting_sort(arr, 99))