class Album:
  """Lớp Album lưu trữ thông tin về một album ca nhạc."""

  def __init__(self, ten_album):
    """Hàm khởi tạo."""
    self.ten_album = ten_album
    self.bai_hat = {}  # Bảng băm lưu trữ các bài hát trong album

  def them_bai_hat(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
    """Hàm thêm bài hát vào album."""
    self.bai_hat[ten_bai_hat] = {
        "ten_nhac_si": ten_nhac_si,
        "ten_ca_si": ten_ca_si,
    }

  def xem_album(self):
    """Hàm hiển thị thông tin của album."""
    print(f"\nTên album: {self.ten_album}")
    print("Danh sách bài hát:")
    for ten_bai_hat, thong_tin_bai_hat in self.bai_hat.items():
      print(f"- {ten_bai_hat}:")
      print(f"    Tên nhạc sĩ: {thong_tin_bai_hat['ten_nhac_si']}")
      print(f"    Tên ca sĩ: {thong_tin_bai_hat['ten_ca_si']}")


class TuDien:
  """Lớp Từ điển dùng để quản lý các album ca nhạc."""

  def __init__(self):
    """Hàm khởi tạo."""
    self.albums = {}  # Bảng băm lưu trữ các album

  def nhap_album(self):
    """Hàm nhập thông tin album."""
    while True:
      ten_album = input("Nhập tên album: ")
      if ten_album in self.albums:
        print("Tên album đã tồn tại, vui lòng nhập tên khác.")
      else:
        break

    album = Album(ten_album)

    while True:
      ten_bai_hat = input("Nhập tên bài hát (hoặc 'q' để quay lại): ")
      if ten_bai_hat.lower() == "q":
        break

      ten_nhac_si = input("Nhập tên nhạc sĩ: ")
      ten_ca_si = input("Nhập tên ca sĩ: ")

      album.them_bai_hat(ten_bai_hat, ten_nhac_si, ten_ca_si)

    self.albums[ten_album] = album

  def xem_album(self, ten_album):
    """Hàm hiển thị thông tin album."""
    if ten_album not in self.albums:
      print(f"Không tìm thấy album có tên '{ten_album}'")
      return

    album = self.albums[ten_album]
    album.xem_album()


# Khởi tạo lớp Từ điển
tu_dien = TuDien()

# Menu chính
while True:
  print("\nMenu:")
  print("1. Nhập album")
  print("2. Xem album")
  print("3. Thoát")

  lua_chon = int(input("Nhập lựa chọn: "))

  if lua_chon == 1:
    tu_dien.nhap_album()
  elif lua_chon == 2:
    ten_album = input("Nhập tên album muốn xem: ")
    tu_dien.xem_album(ten_album)
  elif lua_chon == 3:
    break
  else:
    print("Lựa chọn không hợp lệ.")

