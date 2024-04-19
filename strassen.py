def add_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def split_matrix(A):
    n = len(A)
    n2 = n // 2
    A11 = [[0 for _ in range(n2)] for _ in range(n2)]
    A12 = [[0 for _ in range(n2)] for _ in range(n2)]
    A21 = [[0 for _ in range(n2)] for _ in range(n2)]
    A22 = [[0 for _ in range(n2)] for _ in range(n2)]
    for i in range(n2):
        for j in range(n2):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][j + n2]
            A21[i][j] = A[i + n2][j]
            A22[i][j] = A[i + n2][j + n2]
    return A11, A12, A21, A22

def join_matrices(A11, A12, A21, A22):
    n2 = len(A11)
    n = n2 * 2
    A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n2):
        for j in range(n2):
            A[i][j] = A11[i][j]
            A[i][j + n2] = A12[i][j]
            A[i + n2][j] = A21[i][j]
            A[i + n2][j + n2] = A22[i][j]
    return A

def strassen_matrix_multiply(A, B):
    n = len(A)
    if n <= 32:  # Base case for regular matrix multiplication
        C = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C
    else:
        A11, A12, A21, A22 = split_matrix(A)
        B11, B12, B21, B22 = split_matrix(B)

        M1 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
        M2 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
        M3 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
        M4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
        M5 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
        M6 = strassen_matrix_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
        M7 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

        C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
        C12 = add_matrices(M3, M5)
        C21 = add_matrices(M2, M4)
        C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)

        return join_matrices(C11, C12, C21, C22)

# Example usage:
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]

C = strassen_matrix_multiply(A, B)
for row in C:
    print(row)
