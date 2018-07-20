

def partition(array, begin_i, end_i):
    pivot_i = begin_i #set the pivot as the first index in the array segment
    for curr_i in range(begin_i+1, end_i+1): # iterate over the remaining indicies
        if array[curr_i] <= array[begin_i]:
            pivot_i += 1
            array[curr_i], array[pivot_i] = array[pivot_i], array[curr_i]
    array[pivot_i], array[begin_i] = array[begin_i], array[pivot_i]
    return pivot_i



def quicksort(array, begin=0, end_i=None):
    if end_i is None:
        end_i = len(array) - 1
    def _quicksort(array, begin, end_i):
        if begin >= end_i:
            return
        pivot = partition(array, begin, end_i)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end_i)
    return _quicksort(array, begin, end_i)

[4,3,5,2,1]

# ​def​ ​partition!​(left_pointer, right_pointer)
# ​ ​     ​# We always choose the right-most element as the pivot​​ 
# pivot_position = right_pointer​     pivot = @array[pivot_position]​ ​ 
# ​# We start the right pointer immediately to the left of the pivot​​ 
# right_pointer -= 1​ ​ 
# ​while​ ​true​ ​do​​ ​ 
# ​while​ @array[left_pointer] < pivot ​do​​ 
# left_pointer += 1​       ​
# end​​ ​ 
# ​while​ @array[right_pointer] > pivot ​do​​ 
# right_pointer -= 1​ 
# ​end​​ ​ 

# ​if​ left_pointer >= right_pointer​         ​
# break​​ 
# ​else​​ 
# swap(left_pointer, right_pointer)​ 
# ​end​







"""
1: [4,3,5,2,1] 0, 4





"""
