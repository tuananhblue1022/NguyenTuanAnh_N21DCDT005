class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def isEmpty(self):
        return self.linked_list.head is None

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())  
print(customStack.isEmpty())  
print(customStack.pop())  
print(customStack.peek())  
customStack.delete()
print(customStack.isEmpty()) 
