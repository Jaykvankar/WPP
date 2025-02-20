class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Error: Password must be at least 6 characters long.")
            return False
        if new_password in self.old_passwords:
            print("Error: Password has been used before. Choose a different one.")
            return False
        self.old_passwords.append(new_password)
        print("Password updated successfully.")
        return True

    def is_correct(self, password):
        return password == self.get_password()


def menu():
    manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Set a new password")
        print("2. Verify a password")
        print("3. View password history")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter a new password: ")
            manager.set_password(password)

        elif choice == "2":
            password = input("Enter password to verify: ")
            print("Password is correct!" if manager.is_correct(password) else "Incorrect password.")

        elif choice == "3":
            print("\nPassword history:")
            for i, p in enumerate(manager.old_passwords, start=1):
                print(f"{i}. {p}")

        elif choice == "4":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__=="__main__":
    menu()