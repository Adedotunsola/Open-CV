class Account:
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance


class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__('Savings', balance)

    def deposit(self, amount):
        super().deposit(amount)
        self._balance += amount * 0.005

    def withdraw(self, amount):
        if amount <= 700000:
            self._balance -= amount
        else:
            print("Withdrawal limit exceeded!")


class CurrentAccount(Account):
    def __init__(self, balance=0):
        super().__init__('Current', balance)

    def withdraw(self, amount):
        self._balance -= amount


class ChildrensAccount(Account):
    def __init__(self, balance=0):
        super().__init__('Childrens', balance)

    def deposit(self, amount):
        super().deposit(amount)
        self._balance += amount * 0.007

    def withdraw(self, amount):
        print("Withdrawals are not allowed from Children's Account!")


class StudentAccount(Account):
    def __init__(self, balance=0):
        super().__init__('Student', balance)

    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("Deposit limit exceeded!")

    def withdraw(self, amount):
        if amount <= 2000:
            self._balance -= amount
        else:
            print("Withdrawal limit exceeded!")


# Example usage
savings = SavingsAccount(100000)
savings.deposit(10000)
savings.withdraw(50000)
print("Savings Account Balance:", savings.get_balance())

current = CurrentAccount(100000)
current.deposit(10000)
current.withdraw(50000)
print("Current Account Balance:", current.get_balance())

childrens = ChildrensAccount(100000)
childrens.deposit(10000)
childrens.withdraw(50000)
print("Children's Account Balance:", childrens.get_balance())

student = StudentAccount(100000)
student.deposit(40000)
student.withdraw(1000)
print("Student Account Balance:", student.get_balance())
