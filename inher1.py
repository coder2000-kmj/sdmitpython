#inheritance
# class derived(class base):
class candidate:
    name="";skill=""
    def __str__(self):
        return self.name+" "+self.skill+"\n"
class org(candidate):
    offer=0
    def addMore(self):
        self.offer+=2.3;
    def __add__(self,set):
        self.skill=set;
        if self.skill == 'java' or self.skill=='python':
            self.offer=4.5
        elif self.skill == 'php' or self.skill=='c#':
            self.offer=3.2
        elif self.skill == 'javascript' or self.skill=='ruby':
            self.offer=4.8
        else:
            self.offer=2.3
    def __str__(self):
        return self.name+" "+self.skill+" "+str(self.offer)+"\n"
class assign(org):
    pro={'python':'sdm','java':'mite','c':'ksr','c#':'klu','javascript':'nmamit'}
    def __mul__(self,expect):
        for each in self.pro.keys():
            if self.skill==each:
                print(self.name,"work in",self.pro[each])
#com1=assign();com1.name="Titus";com1+"java";print(com1)
#com2=assign();com2.name="Jincy";com2+"javascript";print(com2)
#com1*'sdm';com2*'klu'
'''
com3=org();com3.name="Apoorva";com3+"c#";print(com3)
com4=org();com4.name="Skandashree";com4+"perl";print(com4)
cOne=candidate();cOne.name="Mohamed";cOne.skill="Python"
print(cOne)
#com1=org();com1.name="Titus";com1.skill="java";com1.offer=4.5
'''
