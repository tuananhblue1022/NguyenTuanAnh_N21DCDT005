class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def KiemTraBST(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        
        if node.info <= min_val or node.info >= max_val:
            return False

        return (self.KiemTraBST(node.left, min_val, node.info) and
                self.KiemTraBST(node.right, node.info, max_val))

    def LaCayBST(self):
        return self.KiemTraBST(self.root)

# Sử dụng đoạn mã
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

# Kiểm tra xem cây có phải là cây BST không
if tree.LaCayBST():
    print("Cây là một cây nhị phân tìm kiếm (BST).")
else:
    print("Cây không phải là một cây nhị phân tìm kiếm (BST).")
