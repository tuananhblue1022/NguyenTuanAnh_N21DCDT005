class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        # Thêm phần tử vào ngăn xếp đầu vào
        self.s1.append(x)

    def dequeue(self):
        # Nếu ngăn xếp đầu ra không rỗng
        if len(self.s2) > 0:
            # Xóa phần tử trên cùng của ngăn xếp đầu ra và trả về
            return self.s2.pop()

        # Nếu ngăn xếp đầu ra rỗng
        else:
            # Chuyển tất cả các phần tử từ ngăn xếp đầu vào sang ngăn xếp đầu ra
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

            # Xóa phần tử trên cùng của ngăn xếp đầu ra và trả về
            return self.s2.pop()


# Ví dụ sử dụng
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # In ra 1
print(q.dequeue())  # In ra 2
print(q.dequeue())  # In ra 3
