sdm={1:"paypal",4:"Evry",2:"Microsoft",5:"Amazon"}
try:
    days = sdm.keys();
    print(days)
    print(days[3])
except TypeError as terror:
    days = tuple(sdm.keys());
    print(days[3])

def check(day=0,count=1):
    try:
        day = int(input("Tell us day: "))
        print(sdm[day]);return;
    except KeyError as kerror:
        print(kerror,"\nTry the different day because given day not available")
        if count<3:count+=1;check(day,count)
        else:return
check()