L=int(input("Enter the value of L: "))
if L<1:
    print("invalid value of L")
    quit()
R=int(input("Enter the value of R: "))
if R<L:
    print("invalid value of R")
    quit()
res=[]
for i in range(L,R+1):
    for j in range(L,R+1):
        if i==j:
            continue
        res.append(i^j)
print(max(res))


