text = input("Enter the string: ")
substring = input("Enter the substring to count: ")

count = 0
i = 0

while i <= len(text) - len(substring):
    if text[i:i+len(substring)] == substring:
        count += 1
    i += 1

print(f"Count: {count}")
