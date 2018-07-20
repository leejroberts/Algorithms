
"""
unrotate the list, then serch it


put in pandas series. sort via value, then perform binary tree, return the index_label



"""
from random import randrange
from math import ceil

lister = list(range(0,100))

def rotate(sorted_list):
    rotation_index = randrange(len(sorted_list))
    return sorted_list[rotation_index:] + sorted_list[:rotation_index]

rotated_list = rotate(lister)

def rotated_search(value_list, value):
    high = len(lister) - 1
    low = 0
    while True:
        middle = ceil(( low + high ) / 2)
        if value == value_list[middle]:
            return middle
        elif low >= high:
            return -1
        elif value_list[low] < value_list[middle]:
            if value < value_list[middle]:
                high = middle
            else:
                low = middle
        elif value_list[middle] < value_list[high]:
            if value > value_list[middle]:
                low = middle
            else:
                high = middle

print("result of rotated search")
print(rotated_search(rotated_list, 101))

print("result of standard search")
print(rotated_list.index(22))
