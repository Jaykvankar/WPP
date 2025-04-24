class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, acc_num, name, balance=0):
        if acc_num in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[acc_num] = {"name": name, "balance": balance}
            print(f"Account created for {name} with balance {balance}.")
    
    def deposit(self, acc_num, amount):
        if acc_num in self.accounts:
            self.accounts[acc_num]["balance"] += amount
            print(f"Deposited {amount}. New balance: {self.accounts[acc_num]['balance']}")
        else:
            print("Account not found.")
    
    def withdraw(self, acc_num, amount):
        if acc_num in self.accounts:
            if self.accounts[acc_num]["balance"] >= amount:
                self.accounts[acc_num]["balance"] -= amount
                print(f"Withdrew {amount}. New balance: {self.accounts[acc_num]['balance']}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")
    
    def display_account(self, acc_num):
        if acc_num in self.accounts:
            acc = self.accounts[acc_num]
            print(f"Account: {acc_num}, Name: {acc['name']}, Balance: {acc['balance']}")
        else:
            print("Account not found.")


bank = Bank()
while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Display Account\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc_num = input("Enter account number: ")
        name = input("Enter account holder's name: ")
        balance = float(input("Enter initial balance: "))
        bank.create_account(acc_num, name, balance)
    elif choice == 2:
        acc_num = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(acc_num, amount)
    elif choice == 3:
        acc_num = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(acc_num, amount)
    elif choice == 4:
        acc_num = input("Enter account number: ")
        bank.display_account(acc_num)
    elif choice == 5:
        break
    else:
        print("Invalid choice, try again.")
