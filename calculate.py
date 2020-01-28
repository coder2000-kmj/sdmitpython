'''
Simple
Script mode
python program
'''

#FD Calculator
money=int(input("Tell us ur desired amount to deposit: "))
tenor=int(input("Tell us ur desired years to deposit: "))
intrest=float(input("Tell us expected intrest rate for : "+str(money)))
maturity=0.0
maturity=(money*intrest)/100
print("Monthly payment: ",(maturity/12))
print("Quaterly payment: ",(maturity/4))
print("Half yearly payment: ",(maturity/2))
print("Yearly payment: ",maturity)
maturity*=tenor;maturity+=money;
print("Maturity as per ur requested: ",maturity)
