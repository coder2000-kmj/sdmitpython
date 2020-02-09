import pickle

from fileaccess.Serialiazation import Lancer

var=open("C:\\Users\\DOLL\\Desktop\\PTest\\SDMIT\\colors.doc","rb");

all=pickle.load(var)

for each in all:
    print(str(each))

var.close()