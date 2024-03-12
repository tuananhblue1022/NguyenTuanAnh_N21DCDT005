class Node:
    def __init__(seft, value):
        seft.value = value
        seft.next = Node

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0

    def append(seft, value):
        new_node = Node(value)
        if seft.head is None:
            seft.head = new_node
            seft.tail = new_node
        else:
            seft.tail.next = new_node
            seft.tail = new_node
        seft.length += 1
new_linked_list = LinkedList()
print(new_linked_list.length)
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list.length)

