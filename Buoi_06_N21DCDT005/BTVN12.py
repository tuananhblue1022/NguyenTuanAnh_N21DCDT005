class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    
    return values == values[::-1]


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print(is_palindrome(head))  
