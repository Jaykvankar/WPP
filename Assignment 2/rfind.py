String=input("Enter a String")
sub_string=input("Enter a Sub String")

length=len(String)
sub_len=len(sub_string)
start=int(input("Enter the start index: "))
end=int(input("Enter the end index: "))
index=-1

for i in range(start,length-sub_len+1):
    if sub_string not in String[start:end]:
        break
    if String[i:i+sub_len]==sub_string:
        index=i
        
print(index)