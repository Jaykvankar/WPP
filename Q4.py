# Swaping 2 Number without third variable
#considering both variable integer

num_1=int(input("Enter Number one : "))
num_2=int(input("Enter Number two : "))

#printing variable before swap

print("Variable before swap")
print(f"number 1 = {num_1}")
print(f"number 2 = {num_2}")

#swaping using arithmatic operation

num_1=num_1+num_2
num_2=num_1-num_2
num_1=num_1-num_2

#printing variable after swap

print("Variable after swap")
print(f"number 1 = {num_1}")
print(f"number 2 = {num_2}")
      