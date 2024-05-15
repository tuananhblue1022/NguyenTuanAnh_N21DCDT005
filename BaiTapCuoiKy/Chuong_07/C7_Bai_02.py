class DoThi:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def them_canh(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def DFS(self, u, visited):
        visited[u] = True
        for v in self.adjacency_list[u]:
            if not visited[v]:
                self.DFS(v, visited)

    def SoThanhPhan(self):
        visited = {vertex: False for vertex in self.vertices}
        count = 0
        for vertex in self.vertices:
            if not visited[vertex]:
                self.DFS(vertex, visited)
                count += 1
        return count

# Sử dụng
dt = DoThi([0, 1, 2, 3, 4, 5])
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(1, 2)
dt.them_canh(1, 3)

print("So luong thanh phan lien thong:", dt.SoThanhPhan())
