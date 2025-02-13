def palindrome(case):
    count=0
    length=len(case)
    mid=length//2
    j=length-1
    for i in range(mid):
        if case[i]!=case[j-i]:
            count+=abs(ord(case[j-i])-ord(case[i]))
        else:
            j=j-1
    return count

def main():
    result=[]
    case=[]
    testcases = int(input("Enter the number of test cases : "))
    for testcase in range(testcases):
        case = (input("Enter the word: "))
        result.append(palindrome(case))
    print(f"the number of changes made: {result}")


if __name__=='__main__':
    main()