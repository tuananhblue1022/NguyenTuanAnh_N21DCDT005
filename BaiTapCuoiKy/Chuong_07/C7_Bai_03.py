class DoThi:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def them_canh(self, u, v):
        self.adjacency_list[u].append(v)
        # Nếu đồ thị là vô hướng, ta cần thêm cạnh về phía ngược lại
        self.adjacency_list[v].append(u)

    def DFS(self, u, visited, parent):
        visited[u] = True
        for v in self.adjacency_list[u]:
            if not visited[v]:
                if self.DFS(v, visited, u):
                    return True
            elif parent != v:
                return True
        return False

    def ChuTrinh(self):
        visited = {vertex: False for vertex in self.vertices}
        for vertex in self.vertices:
            if not visited[vertex]:
                if self.DFS(vertex, visited, -1):
                    return True
        return False

# Sử dụng
dt = DoThi([0, 1, 2, 3,4])
dt.them_canh(0, 1)
dt.them_canh(1, 2)
dt.them_canh(2, 3)
dt.them_canh(2, 4)

if dt.ChuTrinh():
    print("Do thi co chu trinh")
else:
    print("Do thi khong co chu trinh")
