# find the smallest number

array = [ 23, 44, 56, 2, 3, 78, 99, 0 , 12, 33 ]

#pseudo
# store the index of the first number array[0]
# compare the value at the current index, to the next
# store the index of the smaller, repeat until the end of the array is reached

def find_smallest(arr):
    smallest_i = 0
    for i in range(1,len(arr)):
        if arr[smallest_i] > arr[i]:
            smallest_i = i
    return arr[smallest_i]
    
# for index in array:
#     print array[index]

print find_smallest(array)