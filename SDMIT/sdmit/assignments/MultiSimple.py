from threading import *
class Simple(Thread):
    def __init__(self,name=""):
        Thread.__init__(self);self.name=name
    ctc=[4.5,9.2,12.3,2.8,9.1,4.5,6.2]
    def run(self):
        for each in self.ctc:
            if each>=3.0 and each<4.5:
                print("Onsite opprtunity to",each)
            elif each>=4.5 and each<8:
                print("Promoted as Team Lead to",each)
            elif each>=8:
                print(each," You are sack/fired")
            else:
                print(each,"You will be same as you are")

s=Simple();s.start();