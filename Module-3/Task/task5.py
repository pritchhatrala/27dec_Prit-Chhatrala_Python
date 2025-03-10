class father:
    car:int
    bal:int
     
    def getdata(self):
        self.car=input("enter car number:")
        self.bal=input("enter balance :")

class son(father):
    def pritdata(self):
        print("car: ",self.car)
        print("bal: ",self.bal)

sn=son()
sn.getdata()
sn.pritdata()
