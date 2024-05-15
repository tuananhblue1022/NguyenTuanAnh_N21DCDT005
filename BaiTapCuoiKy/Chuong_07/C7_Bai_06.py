class DoThiHuuHuong:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def them_cung(self, u, v):
        self.adjacency_list[v].append(u)

    def SoCungVao(self, v):
        count = 0
        for vertex in self.vertices:
            if v in self.adjacency_list[vertex]:
                count += 1
        return count

# Sử dụng
dt = DoThiHuuHuong([0, 1, 2, 3, 4, 5])
dt.them_cung(0, 1)
dt.them_cung(1, 2)
dt.them_cung(1, 3)
dt.them_cung(2, 3)
dt.them_cung(2, 4)
dt.them_cung(3, 0)
dt.them_cung(4, 1)
dt.them_cung(5, 4)

v = 3
print(f"Số cung vào đỉnh {v}: {dt.SoCungVao(v)}")
