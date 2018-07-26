import pytest

from bi_tree import BinaryTree
from random import shuffle

@pytest.fixture
def random_array():
    randomized_arr = list(range(1, 21))
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

    assert bi_tree.node_count == 20
    assert bi_tree.search(1) is True
    assert bi_tree.search(2) is True
    assert bi_tree.search(8) is True
    assert bi_tree.search(33) is False

def test_remove_from_single_node_bitree():
    # test single value tree removal
    bi_tree = BinaryTree()
    bi_tree.insert(4)
    assert bi_tree.remove(4)
    assert bi_tree.search(4) is False

def test_remove_from_simple_bi_tree():
    # test multi-value tree removal
    bi_tree = BinaryTree(4)
    bi_tree.insert(3)
    bi_tree.insert(5)
    bi_tree.remove(4)
    bi_tree.search(4) is False
    bi_tree.search(3) is True
    bi_tree.search(5) is True

def test_return_node():
    rand_arr = random_array()
    bi_tree = BinaryTree()
    for num in rand_arr:
        bi_tree.insert(num)
    bi_tree.search(5) is True
    bi_tree.return_node(5).value == 5
    bi_tree.return_node(10).value == 10
    bi_tree.return_node(7).value == 7
    bi_tree.return_node(1).value == 1
    bi_tree.return_node(11).value == 11
    bi_tree.return_node(8).value == 8


def test_remove_from_full_bi_tree():
    bi_tree = BinaryTree()
    rand_arr = random_array()
    for num in rand_arr:
        bi_tree.insert(num)
    assert bi_tree.search(5) is True
    bi_tree.remove(5)
    assert bi_tree.search(5) is False
    for num in rand_arr:
        if num != 5:
            assert bi_tree.search(num) is True
