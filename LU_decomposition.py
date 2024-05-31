import numpy as np
from io import StringIO


def LU_decomposition_and_check(A):
    U = A.copy()
    L = np.eye(A.shape[0])
    row = 0
    while row < U.shape[0] - 1:
        # Step 1
        if U[row, row] == 0:
            print(f"Phân tích LU không thể thực hiện được tại hàng {row} (phần tử chéo chính bằng 0).")
            return None, None
        # Step 2
        for i in range(row + 1, U.shape[0]):
            if U[i, row] != 0:
                temp = U[i, row] / U[row, row]
                U[i, row:] = U[i, row:] - temp * U[row, row:]
                L[i, row] = temp
        # Step 3
        row += 1
    # Step 4
    if U[-1, -1] == 0:
        print(f"Phân tích LU không thể thực hiện được tại hàng {U.shape[0]-1} (phần tử chéo chính bằng 0).")
        return None, None
    return L, U


# Đọc ma trận từ chuỗi StringIO
d = StringIO("-1 1 3 1 4 \n 0 -1 2 1 3 \n 1 -1 -3 6 2 \n 2 -2 -4 1 0")
A = np.loadtxt(d, usecols=(0, 1, 2, 3, 4))
print('A =', A)

# Thực hiện phân tích LU và kiểm tra điều kiện
L, U = LU_decomposition_and_check(A)

# In kết quả nếu phân tích LU thành công
if L is not None and U is not None:
    print('L =', L)
    print('U =', U)
    print('LU =', np.dot(L, U))
else:
    print("Ma trận không thể phân tích được thành LU.")
