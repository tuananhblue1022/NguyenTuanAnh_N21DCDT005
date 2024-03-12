class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Tạo danh sách liên kết mới
my_list = LinkedList()

# Chèn các giá trị vào đầu danh sách
my_list.prepend(6)
my_list.prepend(5)
my_list.prepend(4)
my_list.prepend(3)
my_list.prepend(2)
my_list.prepend(1)

# In danh sách liên kết sau khi chèn
print("Danh sách liên kết sau khi chèn:")
my_list.print_list()