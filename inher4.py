#overriding
class base:
    milages=[56,78,25,60,70,45,40]
    def __mul__(self,num):
        print("Milages going to be reduced")
        for each in range(len(self.milages)):
            self.milages[each]-=num
            print(self.milages[each])

class showroom(base):
    def __str__(self):
        return str(self.milages)+"\n"
    def __mul__(self,num):
        super().__mul__(num)
        print("Milages going to be incresed")
        for each in range(len(self.milages)):
            self.milages[each]+=num
            print(self.milages[each])


dealer=showroom();dealer*10;print(dealer)
