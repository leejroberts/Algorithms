

def insertion_sort(array):
    for index in range(1, len(array)): # note that range is exclusive in python
        position = index # position will shift backwards during the inner while loop
        temp_value = array[index] # holds the starting value at the current index

        # you must be at least at index 1 (the second value) to be able to look at the previous value
        # also, if the previous value is lower the sorting (up to the current index) is complete
        # if not, the two values must be switched
        while position > 0 and array[position -1] > temp_value:
            array[position] = array[position -1] # shift the value one position up in the array
            position = position - 1 # move backwards one index in the array and repeat the operation
        # once the sorting is complete for the current index, put the temp_value back into the array
        array[position] = temp_value

    return array
