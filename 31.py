class bankaccount:
    def __init__ (self,balance):
        self._balance = balance
    def deposite(self, amount):
        return self._balance
    
acc =bankaccount(10000)
acc.deposite(500)
print("balance",acc.get_balance())
