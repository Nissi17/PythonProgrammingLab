def credit(balance, balancex):
    balance=balance + balancex
    return balance

def debit(balance,balancex):
    balance=balance-balancex

def showBalance(balance):
    print(balance)


    balancex=input("Enter the credit amount")
    balancey=input("Enter the debit amount")
    balance=0

    balance =credit(2000,balancex)
    balance= debit(300,balancey)
    print(balance)
