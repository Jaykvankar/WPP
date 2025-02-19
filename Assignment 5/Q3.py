t=int(input("Enter the number of testcase: "))
res=[]
for c in range(t):
    w=list(input("Enter the word: "))
    n=len(w)
    i=n-2
    while i >=0 and w[i]>w[i+1]:
        i-=1
    if i==-1:
        res.append("no answer")
    else:
        j=n-1
        while w[i]>=w[j]:
            j-=1
        w[i] , w[j] = w[j] , w[i]
        w = w[:i + 1] + sorted(w[i + 1:])
        res.append("".join(w))

print("\n".join(res))