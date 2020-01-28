# land registration
pin=int(input("Tell us pinCode: "))
area=int(input("Tell us square feet of land: "))
charges=0
if pin >=636001 and pin<=636010:
    charges=2
elif pin >=636011 and pin<=636020:
    charges=4
elif pin >=636031 and pin<=636040:
    charges=5
else:
    charges=8
charges=((area*500)*charges)/100
print("Charges: ",charges)
