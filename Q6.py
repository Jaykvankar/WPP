# Revering a Given Number

num=int(input("Enter a number which will be reversed : "))  # user inputing the number
result=0    # result where revered number will be stored

# Reversing using while loop
while num!=0:
    temp=num%10
    result=result*10+temp
    num//=10
#printing
print(f"The Reversed Number is : {result}")