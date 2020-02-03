class laptop:
    #model="";price=0.0;ram=0;hdd=0;featues=[0]
    "laptop class"
    def __init__(self,mod="",amt=0,rm=0,disk=0,feat=[]):
        self.__model=mod;self.__price=amt;self.__ram=rm;
        self.__hdd=disk;self.__features=feat
    def setModel(self,mod):
        self.__model=mod
    def getModel(self):
        return self.__model
    def setPrice(self,amt):
        self.__price=amt
    def getPrice(self):
        return self.__price
    def setRam(self,rm):
        self.__ram=rm
    def getRam(self):
        return self.__ram
    def setHdd(self,disk):
        self.__hdd=disk
    def getHdd(self):
        return self.__hdd
    def setFeatures(self,feat):
        self.__features=feat
    def getFeatures(self):
        return self.__features
    def __str__(self):
        return self.__model+" "+str(self.__price)+" "+str(self.__ram)+" "+str(self.__hdd)+" "+str(self.__features)+"\n";

print(laptop.__doc__)
one=laptop("Toshiba",37900,4,500,["Corei3","No battery support"]);
print(one)
#print(one.__model)
two=laptop("Vostro",32910,2,250,["Windows7"])
print(two.getModel(),two.getFeatures(),two.getPrice())
