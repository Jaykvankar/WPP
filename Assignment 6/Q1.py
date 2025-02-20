class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    def is_correct(self, password):
        return password == self.get_password()
manager = PasswordManager()
password= input("Enter the password: ")
manager.set_password(password)
print("The password updated")
password= input("Enter new password: ")
manager.set_password(password)
manager.set_password("hi")
print(manager.is_correct(password))

for i in manager.old_passwords:
    print(i)