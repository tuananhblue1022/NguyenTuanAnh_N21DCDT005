class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def SoSanh(self, other_tree):
        def _SoSanh(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return (node1.info == node2.info and
                    _SoSanh(node1.left, node2.left) and
                    _SoSanh(node1.right, node2.right))

        return _SoSanh(self.root, other_tree.root) if isinstance(other_tree, CayNhiPhan) else False

# Sử dụng đoạn mã
# Tạo cây nhị phân 1
tree1 = CayNhiPhan()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)

# Tạo cây nhị phân 2
tree2 = CayNhiPhan()
tree2.root = Node(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)

# So sánh hai cây
if tree1.SoSanh(tree2):
    print("Hai cây giống hệt nhau.")
else:
    print("Hai cây không giống nhau.")
