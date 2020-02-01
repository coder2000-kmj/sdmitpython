class Numeric:
    def __init__(self,al=0,bt=0,cs=0):
        self.__alpha=al;self.__beta=bt;self.__cosmo=cs
    def __str__(self):
        return str(self.__alpha)+" "+str(self.__beta)+" "+str(self.__cosmo)
    def setAlpha(self,al):
        self.__alpha=al
    def getAlpha(self):
        return self.__alpha
    def setBeta(self,bt):
        self.__beta=bt
    def getBeta(self):
        return self.__beta
    def setCosmo(self,cs):
        self.__cosmo=cs
    def getCosmo(self):
        return self.__cosmo
    def shift(self):
        self.__cosmo=self.__alpha<<self.__beta

num=Numeric()
num.setAlpha(12);num.setBeta(4);num.shift();print(num.getCosmo())
