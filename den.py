# denomination

two=int(input("no of 2000's: "));five=int(input("no of 500's: "));one=int(input("no of 100's: "))
tmp=int(input("Required amount: "))
info=str(tmp)+" can be given as following denomination"
if tmp%2000==0 or tmp<=(two*2000) or tmp>=(two*2000) and two>0:
    if two>=(tmp/2000):
        two-=int(tmp/2000)
        info+="\nNo of 2000's are: "+str(int(tmp/2000))
        #print("No of 2000's are: ",int(tmp/2000))
        #print("remaining to find : ",tmp,"remaining 2000 are: ",two)
        tmp-=(int(tmp/2000)*2000)
    else:
        tmp-=int(two*2000);
        info+="\nNo of 2000's are: "+str(two)
        #print("No of 2000's are: ",two);
        two=0
    #print("remaining to find : ",tmp,"remaining 2000 are: ",two)
if tmp>=0 and tmp%500==0 or tmp<=(five*500) or tmp>=(five*500) and five>0:
    if five>=(tmp/500):
        five-=int(tmp/500)
        info+="\nNo of 500's are: "+str(int(tmp/500))
        #print("No of 500's are: ",int(tmp/500))
        tmp-=(int(tmp/500)*500)
    else:
        tmp-=int(five*500);
        #print("No of 500's are: ",five);
        info+="\nNo of 500's are: "+str(five)
        five=0
    #print("remaining to find : ",tmp,"remaining 500 are: ",five)
if tmp>=0 and tmp%100==0 or tmp<=(one*100) or tmp>=(one*100) and one>0:
    if one>=(tmp/100):
        one-=int(tmp/100)
        info+="\nNo of 100's are: "+str(int(tmp/100))
        #print("No of 100's are: ",int(tmp/100))
        tmp-=(int(tmp/100)*100)
    else:
        tmp-=int(one*100);
        info+="\nNo of 100's are: "+str(one)
        #print("No of 100's are: ",one);
        one=0
    #print("remaining to find : ",tmp,"remaining 100 are: ",one)
if tmp>0:
    print("Insufficient to dispense")
else:
    print(info)
