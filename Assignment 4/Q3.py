import re
sen=input("Enter a Paragrams: ")
check=''
sen=sen.lower()
for i in sen:
    if re.search('[a-z]',i):
        check+=i
if len(set(check))==26 :
    print("Is Pangram")
else :
    print("Not a pangram")