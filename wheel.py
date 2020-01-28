# basic pattern
'''
$$$$
$$$$
$$$$
$$$$
$$$$
$$$$
$$$$

'''
for cabin in range(12,5,-1):
    for person in range(1,5):
        print("$",end="")
    print()

'''
$
$$
$$$
$$$$
'''
for cabin in range(1,5):
    for person in range(1,(cabin+1)):
        print("$",end="")
    print()

dish="mcfe"
for cabin in range(len(dish)):
    for person in range(cabin+1):
        print(dish[person],end="")
    print()
