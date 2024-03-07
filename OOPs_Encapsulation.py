class Account:
    def __init__(self , bal,acc):
        self.balance = bal
        self.account = acc
    
    #debit
    def debit(self , amount):
        self.balance -= amount
        print("Rs" , amount , "was debited.")
        print("Total balance is: ", self.get_balance())

    #credit
    def credit(self , amount):
        self.balance += amount
        print("Rs" , amount , "was credited.")
        print("Total balance is: ", self.get_balance())


    def get_balance(self):
        return self.balance

      

acc1 = Account(10000,343434)
acc1.debit(1000)
acc1.credit(40000)