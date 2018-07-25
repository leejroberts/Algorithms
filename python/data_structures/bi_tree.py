
class Node:
    def __init__(self, value=None, left_b=None, right_b=None):
        self.left_b = left_b
        self.value = value
        self.right_b  = right_b

class BinaryTree:
    def __init__(self, value=None):
        self.base = Node(value)
        self.node_count = 1

    def insert(self, value, current_node=None):
        current_node = current_node or self.base

        if current_node.value is None:
            current_node.value = value
            return True
        elif value > current_node.value:
            if current_node.right_b is None:
                current_node.right_b = Node(value)
                self.node_count += 1
                return True
            else:
                current_node = current_node.right_b
                self.insert(value, current_node)
        else:
            if current_node.left_b is None:
                current_node.left_b = Node(value)
                self.node_count += 1
                return True
            else:
                current_node = current_node.left_b
                self.insert(value, current_node)


    def search(self, value, current_node=None):
        """returns true if value present, else false"""
        current_node = current_node or self.base

        if current_node.value == value:
            return True
        elif current_node.value is None:
            return False
        elif value > current_node.value:
            if current_node.right_b is None:
                return False
            else:
                return self.search(value, current_node.right_b)
        else:
            if current_node.left_b is None:
                return False
            else:
                return self.search(value, current_node.left_b)
