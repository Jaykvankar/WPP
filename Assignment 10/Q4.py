import random
import numpy as np

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(n):
    board = [-1] * n
    rows = list(range(n))
    cols = list(range(n))
    random.shuffle(cols)
    for row in rows:
        for col in random.sample(cols, len(cols)):
            if is_safe(board, row, col, n):
                board[row] = col
                break
    return board if -1 not in board else solve(n)

def print_board(board):
    n = len(board)
    for i in range(n):
        print(" ".join("Q" if j == board[i] else "." for j in range(n)))
    print()

solution = solve(8)
print_board(solution)

def generate_magic_square(n):
    if n % 2 == 1:
        magic_square = [[0] * n for _ in range(n)]
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i][j] = num
            i, j = (i - 1) % n, (j + 1) % n
            if magic_square[i][j] != 0:
                i, j = (i + 2) % n, (j - 1) % n
    else:
        magic_square = [[(n * i + j + 1) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if (i < n // 4 or i >= n - n // 4) and (j < n // 4 or j >= n - n // 4) or (n // 4 <= i < n - n // 4 and n // 4 <= j < n - n // 4):
                    magic_square[i][j] = n * n + 1 - magic_square[i][j]
    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(map(str, row)))
    print()

sizes = [4, 5, 6, 7, 8]
for size in sizes:
    print(f"Magic Square for N={size}")
    print_magic_square(generate_magic_square(size))

def cartesian_to_polar(n):
    points = np.random.rand(n, 2) * 20 - 10
    r = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
    theta = np.arctan2(points[:, 1], points[:, 0])
    polar_points = np.column_stack((r, theta))
    return points, polar_points

cartesian, polar = cartesian_to_polar(10)
print("Cartesian Coordinates:")
print(cartesian)
print("\nPolar Coordinates:")
print(polar)
