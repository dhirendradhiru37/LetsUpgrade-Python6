class bank():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
       
    def deposit(self,balance):
        self.balance+=balance
        return self.balance
     
    def withdraw(self,balance):
        if self.balance>=balance:
            self.balance-=balance
        else:
             print("Not Possible to withdraw only "+str(self.balance)+"is available")
        return self.balance
        
acc1=bank('owner1',100)
print("owner name= ",acc1.owner)
print("initial Balance= ",acc1.balance)
print("After Depositing Rs.2000,  Balance is ",acc1.deposit(2000))
print("After Withdraw Rs.1700, balance is ",acc1.withdraw(1700))
acc1.withdraw(700)
