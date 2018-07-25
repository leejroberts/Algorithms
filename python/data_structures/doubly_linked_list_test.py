import pytest

from doubly_linked_list import DoubleLinkedList

@pytest.fixture
def create_beatles():
    beatles = DoubleLinkedList("john")
    beatles.append("paul")
    beatles.append("george")
    beatles.append("ringo")
    return beatles

def test_can_initialize_d_link_list():
    dlink = DoubleLinkedList("steve")
    assert dlink.head.value == "steve"

def test_can_append_values():
    beatles = create_beatles()
    assert beatles.node_count == 4
    assert beatles.head.value == "john"
    assert beatles.tail.value == "ringo"

def test_can_return_value_using_array_syntax():
    beatles = create_beatles()
    assert beatles[0] == "john"
    assert beatles[1] == "paul"
    assert beatles[2] == "george"
    assert beatles[3] == "ringo"
    assert beatles[10] == "index not contained in linked list"

def test_can_set_values_using_array_syntax():
    beatles = create_beatles()
    beatles[0] = "lee"
    assert beatles[0] == "lee"
    beatles[3] = "kyle"
    assert beatles[3] == "kyle"
    beatles[10] = "jake"

def test_can_insert_value():
    beatles = create_beatles()
    beatles.insert_value("lee", 1)
    assert beatles.node_count == 5
    assert beatles[1] == 'lee'
    assert beatles[2] == 'paul'

def test_delete_head():
    beatles = create_beatles()
    beatles.delete_index(0)
    assert beatles.node_count == 3
    assert beatles[0] == 'paul'
    assert beatles.head.value == 'paul'

def test_delete_tail():
    beatles = create_beatles()
    beatles.delete_index(3)
    assert beatles.node_count == 3
    assert beatles.tail.value == "george"

def test_delete_middle_index():
    beatles = create_beatles()
    beatles.delete_index(1)
    assert beatles[1] == "george"
    assert beatles.node_count == 3
