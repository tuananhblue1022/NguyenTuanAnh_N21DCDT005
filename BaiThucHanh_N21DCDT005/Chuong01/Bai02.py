def Neper(n):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)
    
    def term(k):
        return 1 / factorial(k)
    
    if n < 0:
        return "Số nguyên n phải lớn hơn hoặc bằng 0"
    else:
        result = 0
        for k in range(n + 1):
            result += term(k)
        return result

# Kiểm tra phương thức Neper()
n = int(input("Nhập vào số nguyên n: "))
print("Tổng của các số hạng a0 + a1 + ... + an là:", Neper(n))
