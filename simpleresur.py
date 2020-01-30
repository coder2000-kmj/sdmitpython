# simple recursive
def say(count=0):
    if count<=5:
        print("You may not choosen one for today but be like inevitable")
        count+=1;say(count)

def greet(count=1,place=""):
    if count<=5:
        place=input("Where you wish to go: ")
        print("Welcome to ...",place)
        count+=1;greet(count)

def getSum(count=1,sums=0):
    if count<=10:
        num=int(input("Make an entry: "))
        sums+=num;count+=1;getSum(count,sums)
    else:
        print(sums);return

#say()
#greet()
getSum()
