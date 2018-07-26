from random import shuffle

class Node:
    def __init__(self, value=None, left_b=None, right_b=None):
        self.left_b = left_b
        self.value = value
        self.right_b  = right_b

    def has_no_children(self):
        return (self.left_b is None and self.right_b is None)

    def has_both_children(self):
        return (self.left_b and self.right_b)

    def has_any_children(self):
        return (self.left_b or self.right_b)

    def update_attrs_from(self, update_node):
        self.left_b = update_node.left_b
        self.value = update_node.value
        self.right_b = update_node.right_b


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
        node = self.return_node(value, current_node)
        return True if node else False


    def return_node(self, value, current_node=None):
        """returns the node containing the value given if not found returns False"""
        current_node = current_node or self.base

        if current_node.value is None:
            return False
        elif value == current_node.value:
            return current_node
        elif value > current_node.value and current_node.right_b:
            current_node = current_node.right_b
            return self.return_node(value, current_node)
        elif value < current_node.value and current_node.left_b:
            current_node = current_node.left_b
            return self.return_node(value, current_node)
        else:
            return False


    def remove(self, value):

        def remove_rec(starting_node, update_node):
            if update_node.left_b is None:
                starting_node.value = update_node.value
                if update_node.right_b:
                    right_node = update_node.right_b
                    update_node.update_attrs_from(right_node)
                    del right_node
                return True
            else:
                update_node = update_node.left_b
                return remove_rec(starting_node, update_node)

        starting_node = self.return_node(value)
        if not starting_node: # if value was not found
            return False
        elif starting_node.has_no_children():
            starting_node.value = None
            return True
        elif starting_node.left_b and not starting_node.right_b:
            update_node = starting_node.left_b
            starting_node.update_attrs_from(update_node)
            del update_node
            return True
        elif starting_node.right_b:
            update_node = starting_node.right_b
            return remove_rec(starting_node, update_node)

    def print_tree(self):
        current_node = self.base
        if current_node:
            print(current_node.value)
            return self.print_tree(current_node.right_b)
            return self.print_tree(current_node.left_b)
        else:
            return
