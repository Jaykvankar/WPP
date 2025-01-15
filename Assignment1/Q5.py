# Mathematical Table of any number

num=int(input("Enter the number you want table of : ")) # user inputing the number the seek the table of.

print(f"Table of {num} :")

# multipling and printing the result of the multiplication
for i in range(1,11):
    result=num*i
    print(f"{num} x {i} = {result}")
