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
        return max(self.ChieuCao(node.left), self.ChieuCao(node.right)) + 1

    def KiemTraAVL(self, node):
        if node is None:
            return True

        left_height = self.ChieuCao(node.left)
        right_height = self.ChieuCao(node.right)

        if abs(left_height - right_height) <= 1 and \
           self.KiemTraAVL(node.left) and self.KiemTraAVL(node.right):
            return True

        return False

    def LaCayAVL(self):
        return self.KiemTraAVL(self.root)

# Sử dụng đoạn mã
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(7)

# Kiểm tra xem cây có phải là cây AVL không
if tree.LaCayAVL():
    print("Cây là một cây cân bằng AVL.")
else:
    print("Cây không phải là một cây cân bằng AVL.")
