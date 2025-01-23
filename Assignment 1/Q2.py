import random
nums=[]
count=[]
for i in range(100):
    nums.append(random.randint(0,1))
temp=0
print(nums)
for i in range(99):
    if nums[i]==0:
        temp+=1
    else:
        count.append(temp)
        temp=0

print(max(count))
