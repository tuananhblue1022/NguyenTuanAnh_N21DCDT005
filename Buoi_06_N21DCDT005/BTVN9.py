class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicates(head):
    if head is None:
        return
    if head.next and head.value == head.next.value:
        to_free = head.next
        head.next = head.next.next
        removeDuplicates(head)
    else:
        removeDuplicates(head.next)
    return head

def append(head_ref, new_value):
    new_node = Node(new_value)
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

def printList(node):
    while node:
        print(node.value, end=' ')
        node = node.next

# Example usage
head = None
head = append(head, 1)
head = append(head, 1)
head = append(head, 2)
head = append(head, 3)
head = append(head, 3)

print("Linked list before duplicate removal:", end=' ')
printList(head)
head = removeDuplicates(head)
print("\nLinked list after duplicate removal:", end=' ')
printList(head)
