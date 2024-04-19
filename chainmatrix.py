import sys

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n+1) for _ in range(n+1)]
    s = [[0] * (n+1) for _ in range(n+1)]

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end="")
def input_array_from_user():
    array = []
    n = int(input("Enter the size of the array: "))
    print("Enter the elements of the array:")
    for i in range(n):
       element = int(input(f"Enter element {i+1}: "))
       array.append(element)
     
    return array

matrix_dimensions = input_array_from_user()
m, s = matrix_chain_order(matrix_dimensions)
print("Minimum number of multiplications:", m[1][len(matrix_dimensions)-1])
print("Optimal Parenthesization:", end=" ")
print_optimal_parens(s, 1, len(matrix_dimensions)-1)
