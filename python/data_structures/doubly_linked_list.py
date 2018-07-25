

class Node:
    def __init__(self, value=None, previous_node=None, next_node=None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node


class DoubleLinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.tail = self.head
        self.node_count = 1



    def append(self, value):
        """add a value to the end of the list"""
        if self.head.value is None:
            self.head.value = value
        else:
            old_tail = self.tail
            new_tail = Node(value, previous_node=self.tail);
            old_tail.next_node = new_tail
            self.tail = new_tail
            self.node_count += 1


    def return_node_at_index(self, index):
        if index >= self.node_count:
            return None
        elif index is 0:
            return self.head
        elif index == self.node_count - 1:
            return self.tail
        else:
            current_node = self.head
            counter = 0
            while counter < index:
                current_node = current_node.next_node
                counter += 1

            return current_node


    def __getitem__(self, index):
        """array syntax access to indicies"""
        try:
            node = self.return_node_at_index(index)
            return node.value
        except:
            return "index not contained in linked list"


    def __setitem__(self, index, value):
        """array syntax update to indicies"""
        try:
            node = self.return_node_at_index(index)
            node.value = value
        except:
            return "index not contained in linked list"



    def insert_value(self, value, index):
        """inserts a new node with given value at given index"""
        try:
            before_node = self.return_node_at_index(index-1)
            after_node = before_node.next_node
            insert_node = Node(value, before_node, after_node)
            before_node.next_node = insert_node
            after_node.previous_node = insert_node
            self.node_count += 1
        except:
            return "index not contained in linked list"

    def delete_head(self):
        current_head = self.head
        new_head = current_head.next_node
        new_head.previous_node = None
        self.head = new_head
        self.node_count -= 1
        del current_head


    def delete_tail(self):
        current_tail = self.tail
        new_tail = current_tail.previous_node
        new_tail.next_node = None
        self.tail = new_tail
        self.node_count -= 1
        del current_tail


    def delete_index(self, index):
        try:
            if index == 0:
                self.delete_head()
            elif index == self.node_count - 1:
                self.delete_tail()
            else:
                delete_node = self.return_node_at_index(index)
                previous_node = delete_node.previous_node
                next_node = delete_node.next_node
                previous_node.next_node = next_node
                next_node.previous_node = previous_node
                del delete_node
                self.node_count -= 1
        except:
            return "index not contained in linked list"
