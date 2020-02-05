#operator
class store:
    def __init__(self,data=[],tot=0):
        self.__ware=data;self.__sum=sum(self.__ware)
    def __str__(self):
        return str(self.__ware)+" "+str(self.__sum)+"\n"
    def __sub__(self,rside):
        temp=store()
        temp.__sum=self.__sum+rside.__sum
        temp.__ware=(self.__ware+rside.__ware)
        return temp

s1=store([12,45]);print(s1)
s2=store([78,12]);print(s2)
s3=store([67,13]);print(s3)
s4=s1-s2
s4=s4-s3
print(s4)

'''
#operator overloading
class mobile:
    def __init__(self,a="",b=0,c=0.0):
        self.__model=a;self.__price=b;self.__tax=c
    def __str__(self):
        return self.__model+" "+str(self.__price)+" "+str(self.__tax)+"\n"
    def __add__(self,data):
        self.__tax=data
        self.__price+=(self.__price*self.__tax)/100


m1=mobile('realme5s',8000)
m1+6.2;print(m1)
m2=mobile('nokia6.1plus',13000);m2+7.8;print(m2)
'''
