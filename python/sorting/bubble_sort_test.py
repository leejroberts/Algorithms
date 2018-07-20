from bubble_sort import bubble_sort

import pytest

arr = list(range(0,11))
arr.reverse()

def test_bubble_sort():
    assert bubble_sort(arr) == [0,1,2,3,4,5,6,7,8,9,10]
