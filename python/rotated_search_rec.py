# recursive version of rotated_search
from math import ceil


list_1 = list(range(101))
rotated_list = list_1[5:] + list_1[:5]


def rotated_search_rec(value_list, value, low=None, high=None):
    low = low or 0
    high = high or len(value_list) - 1
    middle = ceil((low + high) / 2)
    if low >= high:
        return -1
    elif value == value_list[middle]:
        return middle
    elif value_list[low] < value_list[middle]:
        if value < value_list[middle]:
            return rotated_search_rec(value_list, value, low=low, high=middle)
        else:
            return rotated_search_rec(value_list, value, low=middle, high=high)
    elif value_list[middle] < value_list[high]:
        if value > value_list[middle]:
            return rotated_search_rec(value_list, value, low=middle, high=high)
        else:
            return rotated_search_rec(value_list, value, low=low, high=middle)

print("result of rotated search")
print(rotated_search_rec(rotated_list, 101))

print("result of rotated search")
print(rotated_search_rec(rotated_list, 22))

print("result of standard search")
print(rotated_list.index(22))

