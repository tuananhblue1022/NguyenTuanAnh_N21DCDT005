class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def reverse_linked_list(head):
  prev = None
  current = head

  while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node

  return prev

def print_linked_list(head):
  current = head
  while current:
      print(current.val, end=" -> ")
      current = current.next
  print("None")

linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original Linked List:")
print_linked_list(linked_list)

reversed_linked_list = reverse_linked_list(linked_list)

print("Reversed Linked List:")
print_linked_list(reversed_linked_list)