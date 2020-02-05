#[20 45 60 45 90 100]
from array import *
src=array('i',[20,45,60,45,49,100,49,])
def catch(start=0):
    if start==len(src):return
    else:
        for index in range(start+1,len(src)):
            if src[start]==src[index]:
                x=int(input("Enter the number"))
                if src[start]%x==0:
                    print("The duplicate which / by",x," is",src[start])
                    return
        start+=1;catch(start)
catch();print(src)