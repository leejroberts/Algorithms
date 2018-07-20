import pytest
from random import shuffle

from quick_sort import quick_sort

def test_quick_sort():
    """quick sort should handle a shuffeld array"""
    shuffled_list = list(range(0, 21))
    shuffle(shuffled_list)
    sorted_list = list(range(0,21))
    quick_sort(shuffled_list) # sort occurs in place
    assert shuffled_list == sorted_list

def test_quick_sort_with_duplicate_value():
    shuffled_list = list(range(0,11))
    shuffled_list.append(5)
    shuffle(shuffled_list)
    sorted_list = [0,1,2,3,4,5,5,6,7,8,9,10]
    quick_sort(shuffled_list) # sort occurs in place
    assert None == sorted_list
