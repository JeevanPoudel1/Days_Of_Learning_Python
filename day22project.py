#creating a banking system
class Account:
    def __init__(self, balance, account):
        self.balance= balance
        self.account= account

    #debit amount
    def debit(self, amount):
        self.balance =-amount
        print("Rs.", amount, "was deducted")
        print("total balance = ", self.get_balance())

    #credit amount
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    #get Balance details
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 123456789)
print(acc1.balance)
print(acc1.account)
acc1.debit(1000)
acc1.credit(1500)

acc1.debit(15000)
acc1.credit(18000)
