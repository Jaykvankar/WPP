N=int(input("Number of members:")) #taking input for number of members
count=0
members=[]
# iterating to get height og the number of members
for i in range(N):
    temp=int(input(f"Height of team member {i+1}:"))
    members.append(temp)
# checking to swap if not at their desired input
for i in range(N):
    while members[i]!=i+1:
        temp=members[i]
        members[i]=members[temp-1]
        members[temp-1]=temp
        count+=1
        
print("The minimum number of swaps are:",count)