class laptop:
    #model="";price=0.0;ram=0;hdd=0;featues=[0]
    "laptop class"
    hai=""
    def add(self):
        print("Hell expects ur arraival")
    def insert(self,mod,amt,rm,disk,feat):
        self.__model=mod;self.__price=amt;self.__ram=rm;
        self.__hdd=disk;self.__features=feat
    def show(self):
        print(self.__model,self.__price,self.__ram,self.__hdd,self.__features)

print(laptop.__doc__)
one=laptop();one.hai="Preetham";
one.insert("Toshiba",37900,4,500,["Corei3","No battery support"])
one.show()
#print(one.__model)
two=laptop()
two.insert("Vostro",32910,2,250,["Windows7"])
two.show()
print(hasattr(one,"hai"))
print(getattr(one,"hai"))
setattr(two,"hai","koushal")
print(getattr(two,"hai"))
delattr(one,"hai")
print(getattr(one,"hai"))
