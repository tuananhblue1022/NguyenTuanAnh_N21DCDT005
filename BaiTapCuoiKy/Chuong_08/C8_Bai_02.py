class TuDien:
  """Lớp TuDien là từ điển chứa các từ của một ngôn ngữ tự nhiên (ví dụ tiếng Việt)."""

  def __init__(self):
    """Hàm khởi tạo."""
    self.tudien = {}

  def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
    """Hàm nhập một từ và các từ đồng nghĩa (nếu có) và các từ trái nghĩa (nếu có) của từ này vào từ điển td. Hàm băm là hàm lấy ký tự đầu tiên của một từ."""
    if tu not in self.tudien:
      self.tudien[tu] = {"dong_nghia": dong_nghia, "trai_nghia": trai_nghia}
    else:
      print(f"Từ {tu} đã tồn tại trong từ điển.")

  def DongNghia(self, tu):
    """Hàm trả về một mảng chứa các từ đồng nghĩa của từ cần tra tu có trong từ điển td."""
    if tu in self.tudien:
      return self.tudien[tu]["dong_nghia"]
    else:
      print(f"Từ {tu} không có trong từ điển.")
      return None

  def TraiNghia(self, tu):
    """Hàm trả về một mảng chứa các từ trái nghĩa của từ cần tra tu có trong từ điển td."""
    if tu in self.tudien:
      return self.tudien[tu]["trai_nghia"]
    else:
      print(f"Từ {tu} không có trong từ điển.")
      return None

# Ví dụ sử dụng

tudien = TuDien()

# Nhập từ "từ điển" và các từ đồng nghĩa, trái nghĩa của nó
tudien.NhapTu("từ điển", ["sót", "họ", "ngữ"], ["phi từ điển", "ngữ pháp"])

# Tra cứu từ đồng nghĩa của từ "từ điển"
dong_nghia = tudien.DongNghia("từ điển")
print(f"Từ đồng nghĩa của \"từ điển\": {dong_nghia}")

# Tra cứu từ trái nghĩa của từ "từ điển"
trai_nghia = tudien.TraiNghia("từ điển")
print(f"Từ trái nghĩa của \"từ điển\": {trai_nghia}")
