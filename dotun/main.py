class Account:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Savings")
        self.transaction_limit = 500000

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            print("Transaction limit exceeded for Savings Account")
        else:
            super().withdraw(amount)

class CurrentAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Current")
        self.transaction_limit = 1000000

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            print("Transaction limit exceeded for Current Account")
        else:
            super().withdraw(amount)

class StudentAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Student")
        self.transaction_limit = 100000

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            print("Transaction limit exceeded for Student Account")
        else:
            super().withdraw(amount)

class ChildrenAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Children")
        self.transaction_limit = 50000

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            print("Transaction limit exceeded for Children Account")
        else:
            super().withdraw(amount)


savings_account = SavingsAccount("122334", 10000)
savings_account.deposit(50000)
savings_account.withdraw(2000)
savings_account.check_balance()

current_account = CurrentAccount("345655", 20000)
current_account.deposit(10000)
current_account.withdraw(5000)
current_account.check_balance()

student_account = StudentAccount("776544", 5000)
student_account.deposit(2000)
student_account.withdraw(1000)
student_account.check_balance()

children_account = ChildrenAccount("53453245", 3000)
children_account.deposit(1000)
children_account.withdraw(500)
children_account.check_balance()
