class sanket:
    sid:int
    stech:str

    def s_getdata(self):
        self.sid=input("enter sanket id:")
        self.stech=input("enter sanket technology:")

class ashok:
    aid:int
    atech:str

    def a_getdata(self):
        self.aid=input("enter ashok id:")
        self.atech=input("enter ashok technology:")


class nirav:
    nid:int
    ntech:str

    def n_getdata(self):
        self.nid=input("enter nirav id:")
        self.ntech=input("enter nirav technology:")


class tops(sanket,nirav,ashok):
    def printdata(self):
        print("------------sankets data------------")
        print("sanket's id:",self.sid)
        print("sanket's technology:",self.stech)

        print("nirav's id:",self.nid)
        print("nirav's technology:",self.ntech)

        print("ashok's id:",self.aid)
        print("ashok's technology:",self.atech)

tp=tops()
tp.s_getdata()
tp.n_getdata()
tp.a_getdata()
tp.printdata()