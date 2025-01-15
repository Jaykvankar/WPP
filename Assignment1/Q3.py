# Finding Factorial of a number

factorial=int(input("Enter number to find factorial of : "))

result=1
result=int(result)

# iterating to find factorial using for loop

for i in range(1,factorial+1):
    result*=i

# printing result
print(f"The factorial of {factorial} is : {result}")