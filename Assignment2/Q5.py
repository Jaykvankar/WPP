students=[]

num_students=10

print("Enter the names of the students (max 15 characters each): ")

for i in range(num_students):
    while True:
        name = input(f"Enter name for student {i + 1}: ")
        if len(name) <= 15:
            students.append(name)
            break
        else:
            print("Name is too long! Please enter a name with at most 15 characters.")

print("\nReversed Names of Students:")
for name in students:
    r_name=name[::-1]
    print(r_name)
