import math
def isfibo(num: int) -> bool:
    if num < 0:
        return False
    dig1=5*(num**2)+4
    dig2=5*(num**2)-4

    if int(math.sqrt(dig1))**2==dig1 or int(math.sqrt(dig2))**2==dig2:
        return True
    return False

def main():
    result=[]
    testcase = int(input("Enter testcase:"))
    for i in range(testcase):
        number = int(input("Enter number:"))
        result+=[(isfibo(number))]
    print(result)

if __name__ == "__main__":
    main()
