# Create a Bank account with members account number, name, type of account
# and balance. Write constructor and methods to deposit at the bank and withdraw
# an amount from the bank.

class Bank:
    def __init__(self):
        self.accno = 92003131313
        self.name = 'Anlin Albert'
        self.acc_type = 'Savings'
        self.balance = 0
    
    def deposit(self):
        print()
        deposit = int(input('Enter deposit amount: '))
        self.balance = self.balance + deposit
        print('Account balance =', self.balance)

    def withdraw(self):
        print()
        withdraw = int(input('Enter withdraw amount: '))

        if self.balance < withdraw:
            print('Insufficient funds in account')
        else:
            self.balance = self.balance - withdraw
        
        print('Account balance =', self.balance)

b = Bank()

print('Deposit & Withdrawal')

b.deposit()
b.withdraw()