#strs
'''name="abdul kalam"
for hai in range(len(name)):
    if hai%2!=0:
        tmp=name[hai];tmp=tmp.upper();#print(tmp,end="")
        name=name.replace(name[hai],tmp)
    print(name[hai],end="")
'''
#strs
name="abdul kalam"
names=name.split()
for yet in range(len(names)):
    for ind in range(0,len(names[yet])):
        if ind%2!=0 and yet==0:
            src=names[yet][ind];
            dest=names[yet][ind].upper();
            names[yet]=names[yet].replace(src,dest)
        elif yet==1 and ind%2==0:
            src=names[yet][ind];
            dest=names[yet][ind].upper();
            names[yet]=names[yet].replace(src,dest)
    #print(names[yet]);
name=names[0]+" "+names[1]
print(name)
