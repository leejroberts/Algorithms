class Node:
    """contains the value of the current node and the index of the next node"""
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    """ singley linked list"""
    def __init__(self, value=None):
        self.head = Node(value, None)
        self.node_count = 1


    def return_last_node(self):
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node

        return current_node


    def return_node_at_index(self, index):
        if index >= self.node_count:
            return "index not contained in linked list"
        else:
            current_node = self.head
            curr_index = 0
            while curr_index < index and current_node.next_node:
                current_node = current_node.next_node
                curr_index += 1

        return current_node


    def get_index(self, index):
        return self.return_node_at_index(index).value


    def append(self, value):
        """adds the value to the end of the linked list."""
        current_tail = self.return_last_node()
        new_tail = Node(value)
        current_tail.next_node = new_tail
        self.node_count += 1


    def insert(self, value, index):
        """inserts value at the given index. overwrites the current value at the index"""
        node_to_update = self.return_node_at_index(index)
        node_to_update.value = value


    def delete_last(self):
        """deletes the last node from the linked list"""
        before_last_node = self.return_node_at_index(self.node_count - 2)
        last_node = before_last_node.next_node
        before_last_node.next_node = None
        del last_node
        self.node_count -= 1


    def delete_index(self, index):
        """deletes the node at the given index"""
        if index >= self.node_count:
            return "index not contained in linked list"
        elif index == self.node_count - 1:
            self.delete_last()
        else:
            node_before = self.return_node_at_index(index-1)
            node_before.next_node = node_before.next_node.next_node
            node_to_delete = node_before.next_node
            del node_to_delete


    def print_list(self):
        """prints the values at all nodes"""
        current_node = self.head
        print(current_node.value)
        while current_node.next_node:
            current_node = current_node.next_node
            print(current_node.value)


    def print_last(self):
        """finds the last node in the linked list and prints the value"""
        print(self.return_last_node().value)
