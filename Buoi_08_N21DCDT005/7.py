class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        if self.root is None:
            return False
        else:
            return self._contains(value, self.root)

    def _contains(self, value, curr_node):
        if value == curr_node.value:
            return True
        elif value < curr_node.value:
            if curr_node.left is None:
                return False
            else:
                return self._contains(value, curr_node.left)
        else:
            if curr_node.right is None:
                return False
            else:
                return self._contains(value, curr_node.right)

