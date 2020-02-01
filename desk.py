from pc import laptop
class desk:
    "collection of laptops/pc"
    __stock={}
    def add(self,lap):
        self.__stock[input("Tell us reference for ur laptop: ")]=lap
        print(lap," is added")
    def __str__(self):
        hai=""
        for yet in self.__stock.keys():
            hai+=yet+" "+str(self.__stock[yet])+"\n"
        return hai
    def pickNaffect(self):
        print("Trying to provide the dicount")
        for each in self.__stock.keys():
            if self.__stock[each].getPrice()>35000:
                temp=self.__stock[each].getPrice()-(self.__stock[each].getPrice()*12)/100
                self.__stock[each].setPrice(temp)
    def __sub__(self,obj):
        key1="";key2="";
        for hai in self.__stock.keys():
            if self.__stock[hai]==obj[0]:
                key1=hai
            if self.__stock[hai]==obj[1]:
                key2=hai
        print(key1,key2)
        if key1!="" and key2!="":
            temp=self.__stock[key1]
            self.__stock[key1]=self.__stock[key2]
            self.__stock[key2]=temp
one=laptop("Toshiba",37900,4,500,["Corei3","No battery support"]);
two=laptop("Vostro",32910,2,250,["Windows7"])
dk=desk()
dk.add(one);dk.add(two);print(dk)
dk-[one,two]#swapping
#print(dk);dk.pickNaffect();print(dk)
print(dk)
