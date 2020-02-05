#[20 45 60 45 90 100]
from array import *
#src=array('i',[20,45,60,45,49,100,49])
src=array('i',[3,2,2,5,6,6,7])
def catch(start=0,dup1=0,dup2=0):
    if start==len(src):return
    else:
        for index in range(start+1,len(src)):
            if src[start]==src[index] and dup1==0:
                dup1=src[start];
            elif src[start]==src[index] and dup2==0:
                dup2=src[start];
        if(dup1!=0 and dup2!=0):
            src.append(dup1^dup2);src.pop(src.index(dup1))
            src.pop(src.index(dup2));src.pop(src.index(dup1))
            src.pop(src.index(dup2))
            return
        start+=1;catch(start,dup1,dup2)
catch();print(src)