#recursive - loop

org={10:"Google",2:"Microsoft",5:"Amazon",3:"Dlithe",6:"TCS",1:"Evry India",4:"IBM",8:"Infosys",7:"Wipro",9:"ZOHO"}

def show(key=1):
    if key<=len(org):
        print(key,org[key])
        key+=1;show(key)
    else:
        return

def search(startday=1,endday=10):
    if startday<=endday:
        print(org[startday]);
        startday+=1;search(startday,endday)
    else:
        return
retail=[23500,18900,45900,34800,28100,78100,32000,68000]
def alter(pos=0):
    if pos<len(retail):
        if retail[pos]>=20000 and retail[pos]<40000:
            print("5percecnt");retail[pos]-=(retail[pos]*5)/100
        elif retail[pos]>=40000 and retail[pos]<60000:
            print("3percecnt");retail[pos]-=(retail[pos]*3)/100
        elif retail[pos]>=60000:
            print("2percecnt");retail[pos]-=(retail[pos]*2)/100
        else:
            print("No changes at cost")
        print("After discount: ",retail[pos])
        pos+=1;alter(pos)
    else:
        return
#show()
#search(3,6)
alter();
