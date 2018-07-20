from random import shuffle

array_1 = list(range(0, 101)) # creates list of 100 random integers

shuffle(array_1)

def quick_sort_rec(rand_array):
    if len(rand_array) <= 1:
        return rand_array
    elif len(rand_array) == 2:
        return rand_array if rand_array[0] < rand_array[1] else [rand_array[1], rand_array[0]]
    else:
        pivot = rand_array[0]
        low_array, high_array = [], []
        for num in rand_array[1:]:
            if num <= pivot:
                low_array.append(num)
            if num > pivot:
                high_array.append(num)

    return quick_sort_rec(low_array) + [pivot] + quick_sort_rec(high_array)

print(quick_sort_rec(array_1))



