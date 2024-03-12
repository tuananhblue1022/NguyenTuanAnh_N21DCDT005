class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head):
        if head is None or head.next is None:
            return head

        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rest

    def print(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next

    def append(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

new_Linked_List = LinkedList()
new_Linked_List.append(4)
new_Linked_List.append(3)
new_Linked_List.append(2)
new_Linked_List.append(1)

print("Given linked list:")
new_Linked_List.print()
new_Linked_List.head = new_Linked_List.reverse(new_Linked_List.head)
print("\nReversed linked list:")
new_Linked_List.print()