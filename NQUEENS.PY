def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, result):
    if row == len(board):
        result.append(["".join("Q" if cell == 1 else "." for cell in row) for row in board])
        return
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, result)
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    result = []
    solve_n_queens_util(board, 0, result)
    return result

# Example usage:
n = 4
solutions = solve_n_queens(n)
for i, solution in enumerate(solutions, start=1):
    print(f"Solution {i}:")
    for row in solution:
        print(row)
    print()
