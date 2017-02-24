array = [1,3,5,8,11,13,15,26,67,77,87,89,101]

# pseudo

# finding a number in an sorted array sort ascending
# find the index in the middle of the array
# return that number and check if it is <, >, or == the number
# if middle is greater than the number, update the index of high
    # making it middle_index - 1
        # then call the function again with the updated high
# if middle is less than the number, update the index of low
    # making it middle_index + 1
        # then call the function again
# if middle is == to the number
    # return the index of middle


def binary_search(array, search, low = 0, high = len(array) - 1):
    middle = (low + high) / 2
    if low > high:
        print 'not found'
    elif array[middle] == search:
        print middle
    elif array[middle] > search:
        binary_search(array, search, low = low, high = middle - 1)
    else:
        binary_search(array, search, low = middle + 1, high = high)

binary_search(array, 3)


# def default_check(default = 10, def_2 = 22):
#     print default
#     print def_2
    
# default_check(def_2 = 27)
