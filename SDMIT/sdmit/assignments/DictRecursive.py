post={"Kaushal":"RI","Neha":"Thalisthar","Avinash":"VAO","Preetham":"RTO","Viswanath":"Sub Collector"}
def reverse(refer=[],start=0,end=0):
    if start==end:return
    else:
        key1=refer[start];key2=refer[end]
        temp=post[key1];post[key1]=post[key2];post[key2]=temp
        start+=1;end-=1;reverse(refer,start,end)

def show(refer=[],iterate=0):
    if iterate == len(refer):return
    else:
        key=refer[iterate]
        '''if post[key]=="VAO":
            post[key]="RI"'''
        print(key, post[key])
        iterate+=1;show(refer,iterate)

refer=list(post.keys())
show(refer)
reverse(refer,0,len(refer)-1)
print("After reverse")
show(refer)
'''yet=list(post.keys())
print(post[yet[0]])'''