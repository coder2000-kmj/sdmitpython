from handling.pc import laptop

one=laptop("Inspiron",37900,2,500,["Corei7"]);
two=laptop("Pavilion",49800,4,1024,["Windows10"])
three=laptop("Alien",27900,3,500,["10'inch"])

hai=[one,two,three]

var=open("C:\\Users\\DOLL\\Desktop\\PTest\\SDMIT\\veena.doc","a+");
for each in hai:
    var.write(str(each))
print("Objects written in",var.name)
var.close()