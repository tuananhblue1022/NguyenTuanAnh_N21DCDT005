# Đệ qui
def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)
# Không đệ qui
def gcd_iterative(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# Nhập hai số nguyên dương 
m = int(input("Nhập số nguyên dương thứ nhất= "))
n = int(input("Nhập số nguyên dương thứ hai= "))
# Tính GCD bằng cả hai cách
gcd_recursive_result = gcd_recursive(m, n)
gcd_iterative_result = gcd_iterative(m, n)
# In kết quả
print(f"Ước số chung lớn nhất của {m} và {n} là {gcd_recursive_result} (đệ qui).")
print(f"Ước số chung lớn nhất của {m} và {n} là {gcd_iterative_result} (không đệ qui).")