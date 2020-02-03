class laptop:
    #model="";price=0.0;ram=0;hdd=0;featues=[0]
    "laptop class"
    def add(self):
        print("Hell expects ur arraival")
    def insert(self,mod,amt,rm,disk,feat):
        self.model=mod;self.price=amt;self.ram=rm;
        self.hdd=disk;self.features=feat
    def show(self):
        print(self.model,self.price,self.ram,self.hdd,self.features)


print(laptop.__doc__)
one=laptop()
one.insert("Toshiba",37900,4,500,["Corei3","No battery support"])
one.show()
print(one.model)
two=laptop()
two.insert("Vostro",32910,2,250,["Windows7"])
two.show()
'''
one=laptop()
one.model="Toshiba";one.price=98700.5
two=laptop()
two.ram=4;two.hdd=1024
print(one.model,one.price)
print(two.ram,two.hdd,two.model)
'''
