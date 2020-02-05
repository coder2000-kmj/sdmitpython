#[12,90,34,78,11,90]
from array import *
src=array('i',[12,90,34,78,11,90])
def catch(start=0):
    if start==len(src):return
    else:
        for index in range(start+1,len(src)):
            if src[start]==src[index]:
                src[start]=(src[start-1])+10
                src[index]=(src[index-1])+10
                return
        start+=1;catch(start)

catch();print(src)