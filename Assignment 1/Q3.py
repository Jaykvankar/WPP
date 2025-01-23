length=float(input("Enter the length in feets: "))
menu=[1,2,3,4,5,6,7]
while True :
    print("Enter 1 for convertion to inch")
    print("Enter 2 for convertion to yard")
    print("Enter 3 for convertion to mile")
    print("Enter 4 for convertion to millimeter")
    print("Enter 5 for convertion to centimeter")
    print("Enter 6 for convertion to meter")
    print("Enter 7 for convertion to kilometer")
    target=int(input("Enter your choice: "))
    value=[12,1/3,1/5280,304.8,30.48,0.3048,0.0003048]

    print(length*value[target-1])

    key=input("enter 1 if you want to continue else for exiting press 0: ")
    if key==1:
        continue
    else:
        break


