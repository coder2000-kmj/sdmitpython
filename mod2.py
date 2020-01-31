# using from
from statement import *
def add(start=0,end=10):
    if start<end:
        trans.append(input("Enter the entry either credit/debit: "))
        start+=1;add(start,end)
    else:
        return
def findNPut(start=0,end=len(trans),count=0,fee=0):
    if start<end:
        if trans[start]=="debit":
            count+=1;
            if count>5:
                fee+=20;
        start+=1;findNPut(start,end,count,fee)
    else:
        print("Charges for this month is: ",fee);return
print(trans)
add();
#print(len(trans))
findNPut(0,len(trans));
'''
we here pass start value and end value manually because
initial list of elements count only each function parameter
takes as len
if we done any changes over the list by one function it wont
affect another one, another one always prefer initial list
of values
this drawback can be over comed in OOP since all going to be
part of same class
'''
