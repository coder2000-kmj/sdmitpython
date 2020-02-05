# using threading
import time
from array import *
from threading import *
class store(Thread):
    def __init__(self,name=""):
        Thread.__init__(self);self.name=name
    __data = array('i', [4500, 12900, 3100])
    def show(self):
        print("called by: ",current_thread().name)
        for check in self.__data:
            print(check)
    def more(self,item=0):
        self.__data.append(item);
        print(item, "added by",current_thread().name)
    def erase(self,pos=0):
        self.__data.pop(pos);
        print(pos, " object removed",current_thread().name)
    def run(self):
        print("Person entered is: ",current_thread().name)
        freeze.acquire()
        self.more(int(input("Element to add "+self.name)))
        if current_thread().name=="Kaushal":
            time.sleep(5);
        self.erase(int(input("Index to remove "+self.name)))
        freeze.release()
        self.show()

freeze=Lock()

s1=store("Kaushal");s1.start();#s1.join()
s2=store("Veena");s2.start();#s2.join()
s3=store("Apoorva");s3.start();#s3.join()