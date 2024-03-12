class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_duplicates(self):
        if self.head is None:
            return

        seen_values = {}
        prev = None
        current = self.head

        while current:
            if current.value not in seen_values:
                seen_values[current.value] = True
                prev = current
            else:
                prev.next = current.next
            current = current.next

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)

# Example usage:
new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(4)
new_linked_list.append(4)
new_linked_list.append(5)

print("Original Linked List:")
print(new_linked_list)

new_linked_list.remove_duplicates()

print("Linked List after removing duplicates:")
print(new_linked_list)
