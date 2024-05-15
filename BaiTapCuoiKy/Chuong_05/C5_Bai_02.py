class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def ChieuCao(self, node):
        if node is None:
            return 0
        else:
            left_height = self.ChieuCao(node.left)
            right_height = self.ChieuCao(node.right)
            return max(left_height, right_height) + 1

    def ChieuCaoCay(self):
        return self.ChieuCao(self.root)

# Sử dụng đoạn mã
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(7)

# In ra chiều cao của cây
print("Chiều cao của cây nhị phân là:", tree.ChieuCaoCay())
