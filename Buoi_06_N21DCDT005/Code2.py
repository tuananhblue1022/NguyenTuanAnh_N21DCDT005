class Node:
    def __init__(seft, value):
        seft.value = value
        seft.next = Node

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
