def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
            return False
        if col + (row - i) < len(board) and board[i][col + (row - i)] == 'Q':
            return False
    return True

def solve_queens(board, row):
    if row == len(board):
        print_board(board)
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            if solve_queens(board, row + 1):
                return True
            board[row][col] = '.'
    return False

def eight_queens():
    n = 8
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_queens(board, 0):
        print("No solution exists")
    else:
        print("Solution found!")

eight_queens()