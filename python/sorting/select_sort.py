

def select_sort(arr):
    for current_i in range(0, len(arr)-1):
        lowest_i = current_i # start with lowest index as current index
        next_i = current_i + 1 # get the next index for comparison

        for compare_i in range(next_i, len(arr)):
            if arr[current_i] > arr[compare_i]:
                lowest_i = compare_i

        if current_i != lowest_i: # switch the lowest index and the current index
            arr[current_i], arr[lowest_i] = arr[lowest_i], arr[current_i]

    return arr

print(select_sort([5,4,3,2,1]))
