class Account():
    def __init__(self,owner,balence=0):
        self.owner = owner
        self.balence = balence

    def deposit(self,dep_amt):
        self.balence = self.balence + dep_amt
        print(f"Deposit in your account {dep_amt} to the money")

    def withdrawal(self,wd_amt):
        if self.balence >= wd_amt:
            self.balence = self.balence - wd_amt
            print(f"{wd_amt} withdra successfully ")
        else:
            print("non money")
    def __str__(self):
        return f"Account owner Name :{self.owner} \n Balence in account :{self.balence}"
a=Account('sam',500)
print(a)
a.deposit(100)
print("Balence",a.balence)
a.withdrawal(100)
print("Balence",a.balence)
