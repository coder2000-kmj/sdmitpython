from array import  *
array1=array('i',[10,400,20,50,30])
array2=array('i',[15,25,35,45,55])
array3=array('i',[])
for  each in range(len(array1)):
    array3.append((array1[each]*100)+array2[each])
for one in range(len(array3)):
    for two in range(len(array3)-1-one):
        if(array3[two]>array3[two+1]):
            temp=array3[two];array3[two]=array3[two+1];
            array3[two+1]=temp
print(array3)