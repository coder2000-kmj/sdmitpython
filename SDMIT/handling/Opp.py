from handling.pc import laptop

class easy:
    "Collection of laptop as list"
    __stock=[]
    def add(self,lap):
        self.__stock.append(lap);print(lap.getModel(),"added")
    def __str__(self):
        hai=""
        for each in self.__stock:
            hai+=str(each)+"\n"
        return hai
    def __sub__(self,obj):
        key1=self.__stock.index(obj[0])
        key2=self.__stock.index(obj[1])
        temp=self.__stock[key1]
        self.__stock[key1]=self.__stock[key2]
        self.__stock[key2]=temp
    def __mul__(self,index=0):
        try:
            return self.__stock[index]
        except IndexError as ierror:
            index=int(input("Tell the index <: "+str(len(self.__stock))))
            return self.__stock[index]


one=laptop("Toshiba",37900,4,500,["No battery support"]);
two=laptop("Vostro",32910,2,250,["Windows7"])
three=laptop("Yoga",27900,4,1024,["360'"])
es=easy();es.add(one);es.add(two);#es.add(three);
print("0th index:",es*0);print("Object :",es*2)
try:
    es-[one,three];
except ValueError as v:
    print(v);es.add(three);es-[one,three];
finally:
    print(es)
