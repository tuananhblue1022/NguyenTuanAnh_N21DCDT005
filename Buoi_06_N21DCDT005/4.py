class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1 
        else:
            self.head = None
            self.tail = None
            self.length = 0

new_linked_list = LinkedList()
print(new_linked_list.length)