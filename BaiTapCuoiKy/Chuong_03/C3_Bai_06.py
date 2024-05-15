class Node:
    def __init__(self, he_so, so_mu):
        self.he_so = he_so
        self.so_mu = so_mu
        self.ke_tiep = None

class DaThuc:
    def __init__(self):
        self.head = None

    def them_so_hang(self, he_so, so_mu):
        #Thêm một số hạng mới vào đa thức
        new_node = Node(he_so, so_mu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ke_tiep:
                current = current.ke_tiep
            current.ke_tiep = new_node

    def rut_gon(self):
        #Rút gọn đa thức bằng cách gộp các số hạng có cùng số mũ và loại bỏ các số hạng có hệ số bằng 0
        current = self.head
        while current:
            temp = current.ke_tiep
            while temp:
                if temp.so_mu == current.so_mu:
                    current.he_so += temp.he_so
                    current.ke_tiep = temp.ke_tiep
                temp = temp.ke_tiep
            if current.he_so == 0:
                current = current.ke_tiep
            else:
                current = current.ke_tiep

    def chep(self):
        #Sao chép đa thức hiện tại để tạo một đa thức mới giống hệt
        new_dathuc = DaThuc()
        current = self.head
        while current:
            new_dathuc.them_so_hang(current.he_so, current.so_mu)
            current = current.ke_tiep
        return new_dathuc

    def in_da_thuc(self):
        current = self.head
        while current:
            print(f"{current.he_so}x^{current.so_mu}", end=" ")
            current = current.ke_tiep
        print()

# Ví dụ sử dụng
dathuc1 = DaThuc()
dathuc1.them_so_hang(3, 2)
dathuc1.them_so_hang(-2, 3)
dathuc1.them_so_hang(5, 2)

print("Đa thức 1:")
dathuc1.in_da_thuc()

dathuc2 = dathuc1.chep()

print("Đa thức 2 (sao chép của đa thức 1):")
dathuc2.in_da_thuc()