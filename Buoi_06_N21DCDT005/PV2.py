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

    def tim_phan_tu_thu_n_tu_cuoi(self, n):
        if n <= 0 or self.head is None:
            return None

        con_tro_thu_nhat = self.head
        con_tro_thu_hai = self.head

        # Di chuyển con trỏ thứ hai n vị trí tiếp theo
        for _ in range(n):
            if con_tro_thu_hai is None:
                return None
            con_tro_thu_hai = con_tro_thu_hai.next

        # Di chuyển cả hai con trỏ cho đến khi con trỏ thứ hai đến cuối danh sách
        while con_tro_thu_hai.next:
            con_tro_thu_nhat = con_tro_thu_nhat.next
            con_tro_thu_hai = con_tro_thu_hai.next

        # Con trỏ thứ nhất hiện chỉ vào phần tử thứ N từ cuối
        return con_tro_thu_nhat.value

# Ví dụ sử dụng:
new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)


n = 2
ket_qua = new_linked_list.tim_phan_tu_thu_n_tu_cuoi(n)
if ket_qua:
    print(f"Phần tử thứ {n} từ cuối là: {ket_qua}")
else:
    print(f"Đầu vào không hợp lệ hoặc danh sách quá ngắn.")
