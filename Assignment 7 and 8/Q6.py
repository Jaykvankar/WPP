class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited: ${:.2f}".format(amount))

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print("Withdrew: ${:.2f}".format(amount))

    def display(self):
        print("Account Number: {}".format(self.account_number))
        print("Balance: ${:.2f}".format(self.balance))


if __name__ == "__main__":
    acc_no = input("Enter account number: ")
    balance_str = input("Enter initial balance: ")
    if balance_str.isdigit():
        initial_balance = float(balance_str)
    else:
        initial_balance = 0.0
        print("Invalid balance input, setting balance to 0.0")
    account = BankAccount(acc_no, initial_balance)

    while True:
        print("\nMenu:")
        print("1. Display account details")
        print("2. Deposit funds")
        print("3. Withdraw funds")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account.display()
        elif choice == '2':
            amount_str = input("Enter deposit amount: ")
            if amount_str.isdigit():
                amount = float(amount_str)
                account.deposit(amount)
            else:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            amount_str = input("Enter withdrawal amount: ")
            if amount_str.isdigit():
                amount = float(amount_str)
                account.withdraw(amount)
            else:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")
