from threading import *
class ex(Thread):
    def __init__(self,name=""):
        Thread.__init__(self);self.name=name
    data=[4.5,9.2,12.3,2.8,9.1,4.5,6.2,3.5,9.1,2.4]
    def run(self):
        stop.acquire()
        self.dele()
        print(self.data)
        stop.release()
    def dele(self):
        inp1=int(input("enter the position 1:"))
        inp2 = int(input("enter the position 2:"))
        #for i in range(len(self.data)):
        if inp1<len(self.data) and inp2<len(self.data):
            self.data.pop(inp1)
            self.data.pop(inp2)
        else:print("Can't delete")
stop=Lock()
s1=ex();s1.start();
s2=ex();s2.start();
s3=ex();s3.start();
s4=ex();s4.start();