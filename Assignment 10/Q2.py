import random
def is_safe(b,r,c):
    for i in range(r):
        if b[i]==c or abs(b[i]-c)==abs(i-r):
            return False
    return True
def solve(n):
    sol=[]
    def place(r,b):
        if r==n:
            sol.append(b[:])
            return
        for c in range(n):
            if is_safe(b,r,c):
                b[r]=c
                place(r+1,b)
                b[r]=-1
    b=[-1]*n
    place(0,b)
    return sol
solutions=solve(8)
print(random.choice(solutions))
