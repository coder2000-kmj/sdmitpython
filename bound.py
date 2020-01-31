# array example; insert,index,remove
from array import *
term=array('i',[])
term.insert(0,98)
term.insert(1,12)
term.insert(3,20)
term.insert(2,100)
#update
term[0]=term[0]//4
#list
for check in term:
    print(check)
#search
print("100 located: ",term.index(100))
#remove
print(term)
def findNDelete(maximum,start=0,end=len(term)):
    if start<end:
        if term[start]>maximum:
            term.remove(term[start])
        start+=1;findNDelete(maximum,start,len(term))
    else:
        return
findNDelete(20,0,len(term))
print(term)
