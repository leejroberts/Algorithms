import pytest
from linked_list import LinkedList


@pytest.fixture
def the_beatles_linked_list():
    beatles = LinkedList("john")
    beatles.append("paul")
    beatles.append("george")
    beatles.append("ringo")
    return beatles

def test_can_initialize_linked_list():
    new_list = LinkedList()
    assert new_list.node_count == 1

def test_can_initialize_linked_list_with_value():
    new_list = LinkedList("steve")
    assert new_list.node_count is 1
    assert new_list.head.value == "steve"

def test_can_push_value_to_linked_list():
    new_list = LinkedList("steve")
    new_list.append("john")
    assert new_list.node_count is 2
    assert new_list.return_last_node().value == "john"

def test_can_append_multiple_times():
    beatles = the_beatles_linked_list()
    assert beatles.node_count is 4
    assert beatles.return_last_node().value == "ringo"

def test_can_insert_a_value_at_an_index():
    beatles = the_beatles_linked_list()
    assert beatles.node_count == 4
    beatles.insert("lee", 2)
    assert beatles.return_node_at_index(2).value == "lee"

def test_can_delete_last_index():
    beatles = the_beatles_linked_list()
    beatles.delete_last()
    assert beatles.node_count == 3
    assert beatles.return_last_node().value == "george"
    beatles.print_list()

def test_can_delete_the_second_index():
    beatles = the_beatles_linked_list()
    original_value = beatles.get_index(2)
    next_value = beatles.get_index(3)
    beatles.delete_index(2)
    beatles.get_index(2) != original_value
