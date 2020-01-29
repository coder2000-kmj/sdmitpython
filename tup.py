#tuple: () ; index,count

milages=(56,90,70,67.9,50,50,70,40,40)
#milages=(56,90,70,67.9,'50',50,70,40,'40')

print(milages)
for one in milages:
    print(one)

'''for pos in range(len(milages)):
    print(milages[pos])'''

print(milages.count(70))
#print(milages.index('50'))

desired=int(input("Tell us desired milage: "))

print("Bikes that provides above: ",desired)
for one in milages:
    if one >= desired:
        print(one)
#milages[0]=80
#del milages[1]

get=list(milages)
print(get)
get[1]=20
print(get)
milages=tuple(get)
print(milages)
