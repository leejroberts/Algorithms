import pytest
from select_sort import select_sort

def test_select_sort():
    arr = list(range(0,11))
    arr.reverse()
    assert select_sort(arr) == [0,1,2,3,4,5,6,7,8,9,10]
