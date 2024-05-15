class DoThi:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def them_canh(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def DFS(self, u, v, visited):
        visited[u] = True
        if u == v:
            return True
        for neighbor in self.adjacency_list[u]:
            if not visited[neighbor]:
                if self.DFS(neighbor, v, visited):
                    return True
        return False

    def DuongDi(self, v1, v2):
        visited = {vertex: False for vertex in self.vertices}
        return self.DFS(v1, v2, visited)

# Sử dụng
dt = DoThi([0, 1, 2, 3, 4, 5])
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(1, 3)
dt.them_canh(2, 4)
dt.them_canh(3, 5)
dt.them_canh(4, 5)

v1 = 0
v2 = 5
if dt.DuongDi(v1, v2):
    print(f"Có đường đi từ đỉnh {v1} đến đỉnh {v2}")
else:
    print(f"Không có đường đi từ đỉnh {v1} đến đỉnh {v2}")
