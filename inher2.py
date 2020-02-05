#hierarchy
from inher1 import candidate,org

class dlithe(candidate):
    offer=0.0;role=""
    def __add__(self,knew):
        self.skill=knew
        if self.skill == 'java' or self.skill == 'pyhton' or self.skill == 'javascript':
            self.offer=8.9;self.role="Senior Consultant"
        elif self.skill == 'c#' or self.skill == 'php':
            self.offer=3.2;self.role="Consultant"
        else:
            self.offer=2.8;self.role="Trainee"
    def __str__(self):
        return self.name+" "+self.skill+" "+str(self.offer)+" "+self.role+"\n"
'''
com1=org();com1.name="Titus";com1+"java";print(com1)
com2=dlithe();com2.name="Jincy";com2+"javascript";print(com2)
'''
