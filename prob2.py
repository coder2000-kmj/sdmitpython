one=int(input("Enter the first number"))
two=int(input("Enter the second number"))
count=1;value=one
while count<=5:
    if value%two==0 and value%one==0:
        print(value,end="")
        count+=1
    else:
        print("*",end="")
    value+=one
