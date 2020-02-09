import pickle
class Lancer:
    name="";pay=0
    def __init__(self,nm="",p=0):
        self.name=nm;self.pay=p
    def __str__(self):
        return self.name+" "+str(self.pay)+"\n"

lan1=Lancer("Mohamed",8.9);lan2=Lancer("Titus",7.1);
lan3=Lancer("Murali",2.1);lan4=Lancer("Maheshwaran",3.2);

hey=[lan1,lan2,lan3,lan4]

var=open("C:\\Users\\DOLL\\Desktop\\PTest\\SDMIT\\colors.doc","ab");

'''var.write(str(lan1));var.write(str(lan2));
var.write(str(lan3));var.write(str(lan4));'''
#var.write(str(hey))
'''pickle.dump(lan1);pickle.dump(lan2);
pickle.dump(lan3);pickle.dump(lan4);'''
var.write(pickle.dumps(hey))
print("Objects are written")
var.close()
