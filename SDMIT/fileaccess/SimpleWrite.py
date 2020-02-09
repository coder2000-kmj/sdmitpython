var=open("C:\\Users\\DOLL\\Desktop\\PTest\\SDMIT\\preetham.doc","w");
print(var.closed)
content=input("Say something to Preetham: ")
var.write(content);print("data written in the file",var.name)
var.close()
print(var.closed)