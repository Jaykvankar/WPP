import random
import numpy as np

def safe(board,row,col,n):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==abs(i-row):
            return False
    return True

def solve(n):
    board=[-1]*n
    rows=list(range(n))
    cols=list(range(n))
    random.shuffle(col)
    for row in rows:
        for col in random.sample(cols,len(cols)):
            if safe(board,row,col,n):
                board[row]=col
                break
    return board if -1 not in board else solve(n)

def printboard(board):
    n=len(board)
    for i in range(n):
        print(" ".join("Q"if j==board[i] else "."for j in range(n)))
    print(end="\n")

solution=solve(8)
printboard(solution)


