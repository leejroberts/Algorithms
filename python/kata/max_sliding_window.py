from collections import deque
from random import shuffle
import pdb

array_1 = list(range(1, 100))
shuffle(array_1) # generates a list of random numbers

def find_max(current_window):
    max_value = current_window[0]
    for num in current_window:
        if num > max_value:
            max_value = num
    return max_value

def find_max_sliding_window(array):
    window = deque(array[0:6]) # initializes the deque
    current_max = find_max(window)
    max_list = [current_max]

    for new_num in array[6:]: # keeps from adding numbers already in queue
        leaving_num = window.popleft()
        window.append(new_num)
        if new_num > current_max:
            current_max = new_num
        elif leaving_num >= current_max:
            current_max = find_max(window)
        print(f"window: {window}, max: {current_max}")
        # pdb.set_trace()
        max_list.append(current_max)

    return max_list
print(array_1)
print(find_max_sliding_window(array_1))


