text=input("Enter the string: ")
old=input("Enter the substring to replace: ")
new=input("Enter the substring to replace with: ")
count=input("Enter the number of replacements (leave blank for all): ")

count=int(count) if count else -1
i=0
occurrences = 0
result=""
for i in range(len(text)):
    if text[i:i+len(old)]==old and (count==-1 or occurrences<count):
        result+=new
        i+=len(old)
        occurrences += 1
    else:
        result+=text[i]
        i+=1

print(f"Updated text: {result}")
