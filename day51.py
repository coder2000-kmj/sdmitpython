#day5:1
trans=[12,45,67,12,49,34,56,89,125,23,44,18,66,32]

def findNPut(start=0,end=len(trans),sums=0):
    if start<end:
        if trans[start]%2!=0 or trans[start]%7==0:
            print(trans[start]);sums+=trans[start]
        start+=1;findNPut(start,end,sums)
    else:
        print("Sum of odd and / 7 is: ",sums);return
findNPut();

hey=[[12,45],[56,89]]
print(hey[0][1])
