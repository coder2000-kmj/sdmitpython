# long jump
first,sec,third,meter=0,0,0,0
for people in range(1,11):
    meter=float(input("Distance is: "))
    if meter >= first:
        third=sec;sec=first;
        first=meter
    elif meter >= sec and meter <= first:
        third=sec;sec=meter
    elif meter >= third and meter<=first and meter <= sec:
        third=meter

print(first," will have price of 2000")
print(sec," will have price of 1500")
print(third," will have price of 1000")

