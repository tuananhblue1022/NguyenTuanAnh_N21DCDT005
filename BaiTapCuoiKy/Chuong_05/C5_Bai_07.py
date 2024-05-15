class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def Chep(self, node):
        if node is None:
            return None
        else:
            new_node = Node(node.info)
            new_node.left = self.Chep(node.left)
            new_node.right = self.Chep(node.right)
            return new_node

    def SaoChep(self):
        new_tree = CayNhiPhan()
        new_tree.root = self.Chep(self.root)
        return new_tree

# Sử dụng đoạn mã
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(7)

# Sao chép cây
copied_tree = tree.SaoChep()

# In ra cây sao chép
print("Cây đã sao chép:")
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.info, end=" ")
        in_order_traversal(node.right)
in_order_traversal(copied_tree.root)
