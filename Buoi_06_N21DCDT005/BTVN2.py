class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

# Example usage:
new_linked_list = LinkedList()
new_linked_list.append(20)
new_linked_list.append(30)

print("Before insertion at beginning:")
current_node = new_linked_list.head
while current_node:
    print(current_node.value)
    current_node = current_node.next

new_linked_list.insert_at_beginning(10)

print("After insertion at beginning:")
current_node = new_linked_list.head
while current_node:
    print(current_node.value)
    current_node = current_node.next
