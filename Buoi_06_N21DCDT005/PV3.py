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

    def partition(self, x):
        if self.head is None:
            return

        smaller_head = smaller_tail = None
        greater_head = greater_tail = None

        current = self.head
        while current:
            if current.value < x:
                if smaller_head is None:
                    smaller_head = smaller_tail = current
                else:
                    smaller_tail.next = current
                    smaller_tail = current
            else:
                if greater_head is None:
                    greater_head = greater_tail = current
                else:
                    greater_tail.next = current
                    greater_tail = current
            current = current.next

        if smaller_head is None:
            return greater_head

        smaller_tail.next = greater_head
        if greater_tail:
            greater_tail.next = None

        return smaller_head

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)

# Example usage:
new_linked_list = LinkedList()
new_linked_list.append(3)
new_linked_list.append(5)
new_linked_list.append(8)
new_linked_list.append(5)
new_linked_list.append(10)
new_linked_list.append(2)
new_linked_list.append(1)

x = 5
print("Original Linked List:")
print(new_linked_list)

new_head = new_linked_list.partition(x)

print(f"Linked List after partitioning around {x}:")
partitioned_list = LinkedList()
partitioned_list.head = new_head
print(partitioned_list)
