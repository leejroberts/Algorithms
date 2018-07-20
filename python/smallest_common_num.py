# find smallest common number of three arrays
from math import ceil
list_1 = [6, 7, 10, 25, 30, 63, 64]
list_2 = [-1 ,4 ,5 ,6 ,7 ,8 ,50]
list_3 = [1, 6, 10, 14]

def bi_tree(array, value):
    low = 0
    high = len(array) - 1
    while True:
        middle = ceil((low + high) / 2)
        if low >= high:
            return False
        elif value == array[middle]:
            return True
        elif value < array[middle]:
            high = middle
        elif value > array[middle]:
            low = middle

def find_smallest_common(array_1, array_2, array_3):
    """find smallest common number between three arrays"""
    for num in array_1:
        if bi_tree(array_2, num) and bi_tree(array_3, num):
            return num

print(find_smallest_common(list_1, list_2, list_3))






