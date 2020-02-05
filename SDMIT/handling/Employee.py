class employee:
    def __init__(self,nm="",amt=0):
        self.name=nm;self.salary=amt
    def __str__(self):
        return self.name+" "+str(self.salary)+"\n"

class resource:
    people=[]
    def __str__(self):
        temp=""
        for each in self.people:
            temp+=str(each)+"\n"
        return temp
    def __sub__(self,obj):
        self.people.remove(obj);print(obj,"is removed")
    def __add__(self,index):
        try:return self.people[index]
        except IndexError as ierror:
            print(ierror,"\nIndex less than ",len(self.people))
            index=int(input(""));return self.people[index]

emp1=employee("Mohamed",5.6);emp2=employee("Murali",3.1);
emp3=employee("Razak",9.3);emp4=employee("Sabari",4.2);
res=resource();res.people.append(emp1);res.people.append(emp2);
res.people.append(emp3);#print(res);
print("REturned is: ",res+3)
try:res - emp4;
except ValueError as verror:
    res.people.append(emp4);print("After adding 4th",res)
    res - emp4;
print(res)