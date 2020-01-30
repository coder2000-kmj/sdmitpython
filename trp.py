#dictionary; dict {}
trp={"Sony":8.0,"Colors":10,"Fox":10,"AXN":5,"CNN":8,"Dicovery":9}
print(trp)
#insert
trp["CN"]=7.5
#update
trp["CNN"]=9
#list
print(trp);print(trp.keys());print(trp.values())
print(trp.get("pogo"));print(trp.items())
for pos in trp.keys():
    if trp[pos] >= 8:
        trp[pos]-=2#update
    print(pos,trp[pos])

for one in trp.items():
    print(one)

channel=input("Which channel you hate most: ")
if trp.get(channel,"False"):
    del trp[channel]
print(trp)
