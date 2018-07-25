import pytest

from bi_tree import BinaryTree
from random import shuffle

@pytest.fixture
def random_array():
    randomized_arr = list(range(1, 11))
    shuffle(randomized_arr)
    return randomized_arr

def test_can_initialize_BinaryTree():
    bi_tree = BinaryTree(3)
    assert bi_tree

def test_can_insert_values_into_BinaryTree():
    bi_tree = BinaryTree(3)
    assert bi_tree.node_count == 1
    assert bi_tree.search(3) is True

    bi_tree.insert(5)
    assert bi_tree.node_count == 2
    assert bi_tree.search(5) is True

    bi_tree.insert(4)
    assert bi_tree.node_count == 3
    assert bi_tree.search(4) is True

def test_can_search_values_in_binaryTree():
    bi_tree = BinaryTree()
    rand_arr = random_array()
    for item in rand_arr:
        bi_tree.insert(item)

    assert bi_tree.node_count == 10
    assert bi_tree.search(1) is True
    assert bi_tree.search(2) is True
    assert bi_tree.search(8) is True
    assert bi_tree.search(33) is False
