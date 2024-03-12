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

        current = self.head
        seen_values = {current.value}

        while current.next:
            if current.next.value in seen_values:
                current.next = current.next.next
            else:
                seen_values.add(current.next.value)
                current = current.next

# Example usage:
def print_linked_list(linked_list):
    current = linked_list.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(2)
new_linked_list.append(4)
new_linked_list.append(3)

print("Original Linked List:")
print_linked_list(new_linked_list)

new_linked_list.remove_duplicates()

print("Linked List after removing duplicates:")
print_linked_list(new_linked_list)
