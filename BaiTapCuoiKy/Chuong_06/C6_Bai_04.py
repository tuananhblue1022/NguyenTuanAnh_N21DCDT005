def merge_and_sort(a, b):
    # Kết hợp hai mảng a và b lại với nhau thành một mảng mới
    merged_array = a + b
    
    # Loại bỏ các phần tử trùng lặp trong mảng mới
    merged_array = list(set(merged_array))
    
    # Sắp xếp mảng mới theo thứ tự tăng dần
    merged_array.sort()
    
    return merged_array
# Ví dụ
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = merge_and_sort(a, b)
print(c)