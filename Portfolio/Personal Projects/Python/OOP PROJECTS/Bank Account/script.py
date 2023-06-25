class BankAccount:
    def __init__(self, name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
    
    def Withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def Check_Balance(self):
        return self.balance
    
    def check_account_info(self):
        print(f"name: {self.name}")
        print(f"account number: {self.account_num}")
        print(f"balance: {self.balance}")

person1 = BankAccount("Adam", "123456789", 1000.0)
person2 = BankAccount("Jill", "332254327", 700.0)

while True:
    account_number = input("Please enter your account number (or 'exit' to quit): ")
    
    if account_number == 'exit':
        break

    action = input("What would you like to do? (deposit, withdraw, check balance or check account info): ")

    if account_number == person1.account_num:
        account = person1
    elif account_number == person2.account_num:
        account = person2
    else:
        print("Error. Invalid account number.")
        continue

    if action == 'withdraw':
        amount = float(input("How much would you like to withdraw?: "))
        result = account.Withdraw(amount)
        if result is not None:
            print(result)
    elif action == 'deposit':
        amount = float(input("How much would you like to deposit?: "))
        account.Deposit(amount)
    elif action == 'check balance':
        balance = account.Check_Balance()
        print(f"Current Balance: {balance}")
    elif action == ' check account info':
        account = account.check_account_info()
        print(f'Account info: {account}')
    else:
        print("Error. Invalid action.")