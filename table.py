# else with loop

num=int(input("Tell us which number table you wish: "))
for left in range(1,11):
    print(left,"*",num,"=",(left*num))
else:
    print("requirement is over")
