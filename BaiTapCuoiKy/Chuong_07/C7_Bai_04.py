class DoThi:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def them_canh(self, u, v):
        self.adjacency_list[u].append(v)
        # Nếu đồ thị là vô hướng, ta cần thêm cạnh về phía ngược lại
        self.adjacency_list[v].append(u)

    def ChuaDinh(self, v):
        return v in self.vertices

# Sử dụng
dt = DoThi([0, 1, 2, 3, 4])
dt.them_canh(0, 1)
dt.them_canh(1, 2)
dt.them_canh(2, 3)

v = 5
if dt.ChuaDinh(v):
    print(f"Đỉnh {v} tồn tại trong đồ thị")
else:
    print(f"Đỉnh {v} không tồn tại trong đồ thị")
