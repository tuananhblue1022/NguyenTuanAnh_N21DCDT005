import numpy as np

def DayConDaiNhat(a, b):
    len_a, len_b = len(a), len(b)
    dp = np.zeros((len_a + 1, len_b + 1))

    max_len = 0
    max_index = (0, 0)

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    max_index = (i, j)

    # Tìm dãy con dài nhất
    longest_subsequence = []
    i, j = max_index
    while i > 0 and j > 0 and dp[i][j] > 0:
        longest_subsequence.append(a[i - 1])
        i -= 1
        j -= 1
    longest_subsequence.reverse()

    return longest_subsequence

# Ví dụ sử dụng:
a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
c = DayConDaiNhat(a, b)
print(f"Mảng c chứa dãy con dài nhất: {c}")