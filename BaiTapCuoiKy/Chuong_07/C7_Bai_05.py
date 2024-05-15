class DoThiVoHuong:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def them_canh(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def BacDinh(self, v):
        return len(self.adjacency_list[v])

# Sử dụng
dt = DoThiVoHuong([0, 1, 2, 3, 4])
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(1, 2)
dt.them_canh(2, 3)

v = 3
print(f"Bậc của đỉnh {v} là: {dt.BacDinh(v)}")
