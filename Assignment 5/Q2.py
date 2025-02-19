T=int(input("Enter the number of testcase: "))
while T>10 or T<1:
    print("Invalid input Testcase mustbe within 1 to 10")
    T=int(input("Enter the number of testcase: "))
case=[int(input("Enter the number: ")) for i in range(T)]
res=[]
for i in range(T):
    if case[i]%2==0:
        res.append((case[i]//2)**2)
    else:
        res.append(((case[i]//2)+1)*(case[i]//2))
print(res)
