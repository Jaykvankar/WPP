numbers = list(range(1, 10001)) 
class1 = []
class2 = []
class3 = []
class4 = []
class5 = []
for number in numbers:
    if number % 5 == 0:
        class1.append(number)
    elif number % 5 == 1:
        class2.append(number)
    elif number % 5 == 2:
        class3.append(number)
    elif number % 5 == 3:
        class4.append(number)
    elif number % 5 == 4:
        class5.append(number)

equivalence_classes = class1 + class2 + class3 + class4 + class5
equivalence_classes.sort()
if equivalence_classes == numbers:
    print("Equivalence classes are valid.")