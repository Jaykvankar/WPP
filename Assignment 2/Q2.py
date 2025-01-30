products={}
while True:
    switch=input("Enter y to continue or q to quit: ")
    if switch.lower()=="q":
        break
    name=input("Enter the product's name you want to add: ")
    value=int(input("Enter the product value: "))
    products.update({name:value})

print(products)