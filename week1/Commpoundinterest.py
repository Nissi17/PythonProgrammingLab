# Code for compound intrest

p=float(input("Enter the principal amount : "))
r=float(input("Enter rate of intrest : "))
t=int(input("Enter the years : "))
ci=p*((1+(r/100))**t)-p

print(round(ci,2))
