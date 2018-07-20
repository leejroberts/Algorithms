"""
bubble sort algorithm

time complexity = O(N^2) or quadratic
"""

def bubble_sort(arr):
    # initially the second to last index,
    # keeps from attempting switch with index past the end of the array/list
    last_index_to_check = len(arr) - 2

    while last_index_to_check >= 0 or switch_counter != 0:
        switch_counter = 0

        for current_i, _ in enumerate(arr):
            if current_i > last_index_to_check:
                break
            else:
                next_i = current_i + 1
                if arr[next_i] < arr[current_i]:
                    switch_counter += 1
                    arr[current_i], arr[next_i] = arr[next_i], arr[current_i]

        last_index_to_check -= 1

    return arr
