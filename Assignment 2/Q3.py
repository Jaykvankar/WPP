test_case=int(input("Enter the number of test case: "))
result=[]
count=0
for i in range(test_case):
    number=str(input("Enter the number: "))
    for j in range(len(number)):
        if int(number[j])== 0:
            continue
        if int(number) % int(number[j]) == 0:
            count += 1
    result.append(count)

print(result)
