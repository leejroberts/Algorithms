from math import ceil

list_1 = [1,23,4,5,6,7,8,9,10]



def recursive_search(search_list, search_value, left_i=0, right_i=None):
    right_i = right_i or len(search_list)-1
    middle_i = ceil(sum(left_i, right_i) / 2 )
    if left_i > right_i:
        return -1
    elif search_value == search_list[middle_i]:
        return middle_i
    elif search_value > search_list[middle_i]:
        left_i = middle_i + 1
    elif search_value < search_list[middle_i]:
        right_i = middle_i - 1
    recursive_search(search_list, search_value, left_i=left_i, right_i=right_i)

