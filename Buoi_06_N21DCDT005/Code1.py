class Node:
    def __init__(seft, value):
        seft.value = value
        seft.next = Node

new_node = Node(10)
print(new_node)
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_linked_list = LinkedList(10)
print(new_linked_list)
print(new_linked_list.head.value)
