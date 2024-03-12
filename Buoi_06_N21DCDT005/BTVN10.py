class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_elements(head, val):
    # Xử lý các trường hợp cần cắt bỏ phần đầu
    while head and head.value == val:
        head = head.next

    current = head

    while current and current.next:
        if current.next.value == val:
            current.next = current.next.next
        else:
            current = current.next

    return head
# Tạo danh sách liên kết
linked_list = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
print("Danh sách liên kết gốc:")
current_node = linked_list
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("Không có")

# Xóa các nút có giá trị 6
linked_list = remove_elements(linked_list, 6)
print("Danh sách liên kết sau khi loại bỏ các nút có giá trị 6::")
current_node = linked_list
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("Không có")
