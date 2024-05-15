class TuDien:
    def __init__(self):
        self.tu_dien = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        """
        Hàm nhập từ vào từ điển.

        Tham số:
            tu (str): Từ cần nhập.
            dong_nghia (str, optional): Từ đồng nghĩa của `tu`. Mặc định là None.
            trai_nghia (str, optional): Từ trái nghĩa của `tu`. Mặc định là None.

        Trả về:
            None.
        """
        tu_dau = tu[0].lower()
        if tu_dau not in self.tu_dien:
            self.tu_dien[tu_dau] = {}
        self.tu_dien[tu_dau][tu] = {"dong_nghia": dong_nghia, "trai_nghia": trai_nghia}

    def TraTu(self, tu):
        """
        Hàm tra cứu từ trong từ điển.

        Tham số:
            tu (str): Từ cần tra cứu.

        Trả về:
            dict: Từ điển chứa thông tin về từ cần tra cứu, bao gồm:
                * "dong_nghia": Từ đồng nghĩa.
                * "trai_nghia": Từ trái nghĩa.

            None nếu từ không có trong từ điển.
        """
        tu_dau = tu[0].lower()
        if tu_dau not in self.tu_dien or tu not in self.tu_dien[tu_dau]:
            return None
        return self.tu_dien[tu_dau][tu]

tu_dien = TuDien()

# Nhập một số từ vào từ điển
tu_dien.NhapTu("con mèo", "mèo", "chó")
tu_dien.NhapTu("con chó", "chó", "mèo")
tu_dien.NhapTu("con ngựa", "ngựa", "lừa")

# Nhập từ từ bàn phím
tu_moi = input("Nhập từ mới: ")
dong_nghia = input("Nhập từ đồng nghĩa (nếu có): ")
trai_nghia = input("Nhập từ trái nghĩa (nếu có): ")

# Thêm từ mới vào từ điển
tu_dien.NhapTu(tu_moi, dong_nghia, trai_nghia)

# Tra cứu thông tin của từ vừa nhập
thong_tin_tu_moi = tu_dien.TraTu(tu_moi)

# In ra thông tin
if thong_tin_tu_moi:
    print(f"Từ đồng nghĩa của '{tu_moi}': {thong_tin_tu_moi['dong_nghia']}")
    print(f"Từ trái nghĩa của '{tu_moi}': {thong_tin_tu_moi['trai_nghia']}")
else:
    print(f"Từ '{tu_moi}' không có trong từ điển.")

    