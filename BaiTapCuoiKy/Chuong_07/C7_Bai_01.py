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

    def LienThong(self):
        visited = {vertex: False for vertex in self.vertices}
        start_vertex = next(iter(self.vertices))  # Lấy một đỉnh bất kỳ làm đỉnh xuất phát
        self.DFS(start_vertex, visited)
        # Kiểm tra xem tất cả các đỉnh đã được duyệt qua không
        for vertex in self.vertices:
            if not visited[vertex]:
                return False
        return True

# Sử dụng
dt = DoThi([ 1, 2, 3])
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(1, 2)
dt.them_canh(2, 3)

if dt.LienThong():
    print("Do thi lien thong")
else:
    print("Do thi khong lien thong")
