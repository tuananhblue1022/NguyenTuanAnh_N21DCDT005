class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def CayCon(self, other_tree):
        def _CayCon(node1, node2):
            if node2 is None:
                return True
            if node1 is None:
                return False
            if node1.info == node2.info:
                return (_CayCon(node1.left, node2.left) and
                        _CayCon(node1.right, node2.right))
            return False

        return _CayCon(self.root, other_tree.root) if isinstance(other_tree, CayNhiPhan) else False

# Sử dụng đoạn mã
# Tạo cây nhị phân 1
tree1 = CayNhiPhan()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)

# Tạo cây nhị phân 2
tree2 = CayNhiPhan()
tree2.root = Node(2)
tree2.root.left = Node(4)
tree2.root.right = Node(5)

# Kiểm tra xem cây 2 có phải là cây con của cây 1 không
if tree1.CayCon(tree2):
    print("Cây 2 là cây con của cây 1.")
else:
    print("Cây 2 không phải là cây con của cây 1.")
