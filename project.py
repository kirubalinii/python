class ATM:
    def __init__(self,balance=500):
        self.balance=balance
    def check_balance(self):
        return f"your account balance is ${self.balance}"
    def deposit(self,amount):
        self.balance+=amount
        return f"deposite $ {amount}.your new balance is ${self.balance}"
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return f"withdraw ${amount}.your new balan is ${self.balance}"
        else:
             return "insufficient funds. withdrawal failed"
atm=ATM()
while True:
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
    choice=input("Enter your choice :")
    if choice=="1":
      print(atm.check_balance())
    elif choice=="2":
      amount=float(input("enter the deposit amount"))
      print(atm.deposit(amount))
    elif choice=="3":
      amount=float(input("enter the withdraw amount"))
      print(atm.withdraw(amount))
    elif choice=="4":
      print("thank you for using the atm")
      break
    else:
      print("invalide choice.pls")
        
amo=input("enter the dollers")
amo=float(amo)
d=amo*79.5
print("the doller is:",amo)
print("coverting a doller into indian rupes:",d)
