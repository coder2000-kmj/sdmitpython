# bubble sort with recursive

price=[126.8,11.4,678.3,567.1,34.7,110.6]

def swap(count,start=0):
    if start < len(price)-count-1:
        if price[start] > price[start+1]:
            price[start]*=price[start+1]
            price[start+1]=price[start]/price[start+1]
            price[start]/=price[start+1]
        start+=1;swap(count,start)
    else:
        return

def times(count=0):
    if count<len(price)-1:
        swap(count);count+=1;times(count)
    else:
        return
def bubble():
    for hai in range(0,len(price)):
        for yet in range(0,len(price)-hai-1):
            if price[yet]>price[yet+1]:
                price[yet]*=price[yet+1]
                price[yet+1]=price[yet]/price[yet+1]
                price[yet]/=price[yet+1]
print(price);
bubble()#times();
print(price)
