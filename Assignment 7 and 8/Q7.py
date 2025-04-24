import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def rotation(self):
        return math.atan2(self.y, self.x)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) * (self.x - other.x) +
                         (self.y - other.y) * (self.y - other.y))

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        Vector2D.__init__(self, x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def rotation(self):
        # Returns the angle between the vector and the x-axis in 3D.
        mag = self.magnitude()
        if mag == 0:
            return 0
        return math.acos(self.x / mag)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) * (self.x - other.x) +
                         (self.y - other.y) * (self.y - other.y) +
                         (self.z - other.z) * (self.z - other.z))

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


def work_with_2d():
    print("\nEnter details for 2D Vector 1:")
    x1 = input("  x: ")
    if not x1.isdigit():
        print("  Invalid input, setting x to 0")
        x1 = 0
    else:
        x1 = float(x1)
    y1 = input("  y: ")
    if not y1.isdigit():
        print("  Invalid input, setting y to 0")
        y1 = 0
    else:
        y1 = float(y1)

    print("\nEnter details for 2D Vector 2:")
    x2 = input("  x: ")
    if not x2.isdigit():
        print("  Invalid input, setting x to 0")
        x2 = 0
    else:
        x2 = float(x2)
    y2 = input("  y: ")
    if not y2.isdigit():
        print("  Invalid input, setting y to 0")
        y2 = 0
    else:
        y2 = float(y2)

    v1 = Vector2D(x1, y1)
    v2 = Vector2D(x2, y2)

    while True:
        print("\n2D Vector Menu:")
        print("1. Display Vector 1 details")
        print("2. Display Vector 2 details")
        print("3. Compute distance between Vector 1 and Vector 2")
        print("4. Compute dot product of Vector 1 and Vector 2")
        print("5. Compute cross product of Vector 1 and Vector 2")
        print("6. Go back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Vector 1:", v1)
            print("  Magnitude:", v1.magnitude())
            print("  Rotation (radians):", v1.rotation())
        elif choice == '2':
            print("Vector 2:", v2)
            print("  Magnitude:", v2.magnitude())
            print("  Rotation (radians):", v2.rotation())
        elif choice == '3':
            print("Distance between Vector 1 and Vector 2:", v1.distance_to(v2))
        elif choice == '4':
            print("Dot product:", v1.dot(v2))
        elif choice == '5':
            print("Cross product:", v1.cross(v2))
        elif choice == '6':
            break
        else:
            print("Invalid choice.")


def work_with_3d():
    print("\nEnter details for 3D Vector 1:")
    x1 = input("  x: ")
    if not x1.isdigit():
        print("  Invalid input, setting x to 0")
        x1 = 0
    else:
        x1 = float(x1)
    y1 = input("  y: ")
    if not y1.isdigit():
        print("  Invalid input, setting y to 0")
        y1 = 0
    else:
        y1 = float(y1)
    z1 = input("  z: ")
    if not z1.isdigit():
        print("  Invalid input, setting z to 0")
        z1 = 0
    else:
        z1 = float(z1)

    print("\nEnter details for 3D Vector 2:")
    x2 = input("  x: ")
    if not x2.isdigit():
        print("  Invalid input, setting x to 0")
        x2 = 0
    else:
        x2 = float(x2)
    y2 = input("  y: ")
    if not y2.isdigit():
        print("  Invalid input, setting y to 0")
        y2 = 0
    else:
        y2 = float(y2)
    z2 = input("  z: ")
    if not z2.isdigit():
        print("  Invalid input, setting z to 0")
        z2 = 0
    else:
        z2 = float(z2)

    u1 = Vector3D(x1, y1, z1)
    u2 = Vector3D(x2, y2, z2)

    while True:
        print("\n3D Vector Menu:")
        print("1. Display Vector 1 details")
        print("2. Display Vector 2 details")
        print("3. Compute distance between Vector 1 and Vector 2")
        print("4. Compute dot product of Vector 1 and Vector 2")
        print("5. Compute cross product of Vector 1 and Vector 2")
        print("6. Go back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Vector 1:", u1)
            print("  Magnitude:", u1.magnitude())
            print("  Rotation (angle with x-axis in radians):", u1.rotation())
        elif choice == '2':
            print("Vector 2:", u2)
            print("  Magnitude:", u2.magnitude())
            print("  Rotation (angle with x-axis in radians):", u2.rotation())
        elif choice == '3':
            print("Distance between Vector 1 and Vector 2:", u1.distance_to(u2))
        elif choice == '4':
            print("Dot product:", u1.dot(u2))
        elif choice == '5':
            cross = u1.cross(u2)
            print("Cross product:", cross)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    while True:
        print("Main Menu:")
        print("1. Work with 2D Vectors")
        print("2. Work with 3D Vectors")
        print("3. Exit")
        main_choice = input("Enter your choice: ")

        if main_choice == '1':
            work_with_2d()
        elif main_choice == '2':
            work_with_3d()
        elif main_choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")
