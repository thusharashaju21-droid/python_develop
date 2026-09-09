class Bank:
    account_number: float
    balance: float
    account_type: str
    customer_name: str

    def __init__(self, account_number, balance, account_type, customer_name):

        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.customer_name = customer_name

    def deposit(self, amount):

        self.balance += amount

        print(f"Your {self.account_number} has been credited with {amount} Available balance is {self.balance}")

    def withdraw(self, amount):

        if self.balance < amount:
            raise Exception("Insufficient balance")

        else:
            self.balance -= amount

            print(f"Your {self.account_number} is debited with {amount} Available balance is {self.balance}")

    def get_balance(self):

        print("Available balance is", self.balance)


bank_instance1 = Bank(1234567, 23000, "savings", "Thushara")
bank_instance1.deposit(2000)
bank_instance1.withdraw(500)

bank_instance1.get_balance()