from array import *
access=array('i',[4,2,6,7,2,5])
min1=access[0];min2=access[0];
for index in range(len(access)):
    if access[index] < min1 and access.count(access[index])<2:
        min2=min1;min1=access[index];
    if access[index] != min1 and access.count(access[index])<2:
        min2=access[index]
print(min1,min2)
in1=access.index(min1);in2=access.index(min2)
access[in1]^=access[in2];access[in2]^=access[in1];
access[in1]^=access[in2];
print(access)