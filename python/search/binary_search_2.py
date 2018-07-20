from math import ceil
import pdb

# given a sorted array of integers, return the index of the given key. Return -1
# if not found


sorted_list = [1,3,4,6,7,44,66,67,88,199,2000]

# how to do this,


def binary_search(search_list, search_value):
    low = 0
    high = len(search_list) - 1
    searching = True
    while searching:
        if low > high:
            return -1
        middle = ceil((low + high) / 2) # starts at the middle index
        current_value = search_list[middle]
        if search_value == current_value:
            return middle
        elif search_value < current_value:
            high = middle - 1
        elif search_value > current_value:
            low = middle + 1

print(binary_search(sorted_list, 88))

print(binary_search(sorted_list, 43))



