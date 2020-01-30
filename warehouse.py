# rercursive

warehouse=[0]

def details(index=0):
    if index<len(warehouse):
        print(warehouse[index])
        index+=1;details(index)
    else:
        return

def update(index=0,end=len(warehouse)):
    if index<end:
        decide=input("Tell us what you wish to do: ")
        if decide=="take":
            amt=int(input("Tell us money wish to take: "))
            if amt>=warehouse[index]:
                warehouse.append(0)
            else:
                warehouse.append(warehouse[index]-amt)
        elif decide =="give":
            amt=int(input("Tell us money wish to give: "))
            warehouse.append(warehouse[index]+amt)
        else:
            print("Check the amount later")
        index+=1;update(index,end)
    else:
        return
            
update(0,4)
details()
