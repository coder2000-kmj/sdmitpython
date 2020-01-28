#nested loop
for lab in range(1,5):
    count=1
    while count<=10:
        ram=int(input("Tell us ram size: "))
        if ram >=4:
            print("Pc arranged @",count,"in the lab:",lab)
            count+=1
