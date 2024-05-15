class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self, node):
        if node is None or (node.left is None and node.right is None):
            return 0
        elif node.left is not None or node.right is not None:
            return 1 + self.SoNutTrungGian(node.left) + self.SoNutTrungGian(node.right)

    def TongSoNutTrungGian(self):
        return self.SoNutTrungGian(self.root)

# Sử dụng đoạn mã
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.right = Node(4)
tree.root.right.left = Node(5)
tree.root.right.right = Node(6)

# In ra số nút trung gian của cây
print("Số nút trung gian của cây nhị phân là:", tree.TongSoNutTrungGian())
