class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    # Create a dummy node to start the merged list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists and merge
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes of list1 or list2, if any
    current.next = list1 if list1 else list2
    
    # Return the head of the merged list (excluding the dummy node)
    return dummy.next

# Example usage:
# Constructing two sample sorted linked lists: 1->2->4 and 1->3->4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged_list = merge_two_lists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
