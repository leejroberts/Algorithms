
def partition(arr, low_i, high_i):
    """mutates an array so that values lower than the pivot_value are moved to it's left
    and the values higher are moved to it's right."""

    pivot_i = high_i
    pivot_value = arr[pivot_i]
    high_i -= 1
    while True:
        while arr[low_i] < pivot_value:
            low_i += 1
        while arr[high_i] > pivot_value:
            high_i -= 1
        if low_i >= high_i:
            break
        arr[low_i], arr[high_i] = arr[high_i], arr[low_i]

    arr[low_i], arr[pivot_i] = arr[pivot_i], arr[low_i]
    return low_i # low_i is now the pivot position, return the pivot postition


def quick_sort(arr, low_i=0, high_i=None):
    if high_i == None:
        high_i = len(arr) - 1 #supplies the default high index (last index)

    if high_i - low_i <= 0:
        return # this partition is complete, you can't sort 0 or 1 items

    pivot_i = partition(arr, low_i, high_i)
    quick_sort(arr, low_i, pivot_i-1) # low parition sort
    quick_sort(arr, pivot_i+1, high_i)  # high partition sort
