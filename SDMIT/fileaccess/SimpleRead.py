var=open("C:\\Users\\DOLL\\Desktop\\MechJava\\kamali.xml","r");
print("data in the file",var.name," is\n",var.read())
print("First 10 characters: ",var.read(10))
print("10 characters: ",var.read(var.seek(10,0)))
var.close()
print(var.closed)