class Bank:
    def __init__(self,accno,name,type,bal):
        self.accno=accno
        self.name=name
        self.type=type
        self.bal=bal
    def deposite(self,amt):
        if amt<=0:
            print("enter a positive number")
        else:
            self.bal+=amt
            print("your current balence is:",self.bal)
    def withdraw(self,amt):
        if amt<=0:
            print("enter a positive number")
        elif amt>self.bal:
            print("insuffucient balence")
        else:
            self.bal-=amt
            print("your current balence is=",self.bal)
    def display(self):
        print("your account number is:",self.accno)
        print("account holder name is :",self.name)
        print("account type is:",self.type)
        print("current balence:",self.bal)
no=int(input("enter your account number:"))
name=input("enter your name:")
type=input("enter your account type:")
bal=int(input("enter your current balence:"))
usr1=Bank(no,name,type,bal)
while True:
    print("1.deposite\n2.withdrawal\n3.account details\n4.exit\n")
    opt=int(input("enter your with option"))
    if opt==1:
        amt=int(input("enter your  amount"))
        usr1.deposite(amt)
    elif opt==2:
        amt = int(input("enter your withdrawal amount"))
        usr1.withdraw(amt)
    elif opt==3:
        usr1.display()
    elif opt==4:
        exit(0)
    else:
        print("invalid option")
