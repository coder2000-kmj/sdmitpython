'''
boeg
boe
bo
b
'''
ser="boeg"
leng=0
for time in range(5,9):
    if time==5:
        leng=len(ser)
    elif time==6:
        leng=len(ser)-1
    elif time==7:
        leng=len(ser)-2
    elif time==8:
        leng=len(ser)-3
    for one in range(leng):
        print(ser[one],end="")
    print()

dish="mcfe"
for cabin in range(len(dish)-1,-1,-1):
    for person in range(cabin+1):
        print(dish[person],end="")
    print()

'''
   m
  mc
 mcf
mcfe
'''
for row in range(0,4):
    for space in range(len(dish)-1,row,-1):
        print(" ",end="")
    for data in range(row+1):
        print(dish[data],end="")
    print()

'''
mcfe
 mcf
  mc
   m
'''
for row in range(len(dish)-1,-1,-1):
    for space in range(len(dish)-1,row,-1):
        print(" ",end="")
    for data in range(row+1):
        print(dish[data],end="")
    print()

for row in range(0,4):
    for space in range(len(dish)-1,row,-1):
        print(" ",end="")
    for data in range(row+1):
        print(dish[data],end=" ")
    print()

for row in range(len(dish)-1,-1,-1):
    for space in range(len(dish)-1,row,-1):
        print(" ",end="")
    for data in range(row+1):
        print(dish[data],end=" ")
    print()






row=int(input("Enter the no of floors u want: "))
limit=1
for count in range(1,(row+1)):
    for space in range(row-1,count-1,-1):
        print(" ",end="")
    for data in range(1,limit+1):
        print("#",end="")
    limit+=2;print()


row=int(input("Enter the no of floors u want: "))
limit=(row*2)-1
for count in range(row,0,-1):
    for space in range(row-1,count-1,-1):
        print(" ",end="")
    for data in range(1,limit+1):
        print("#",end="")
    limit-=2;print()
