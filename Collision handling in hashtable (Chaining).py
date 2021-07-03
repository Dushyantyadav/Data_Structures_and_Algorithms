class myhashexp:
    def __init__(self):
        self.maxitem=10
        self.myarray=[[] for i in range(0,self.maxitem)]

    def myhashfunction(self,key):
        h=0
        for cr in key:
            h=h+ord(cr)
        return h% self.maxitem

    def addvaluefunction(self,key,value):
        h=self.myhashfunction(key)
        found=False

        for idx,element in enumerate(self.myarray):
            if len(element)==2 and element[0]==key:
                self.myarray[h][idx]=(key,value)
                found=True

        if not found:
            self.myarray[h].append((key,value))

    def getthevalue(self,key):
        h=self.myhashfunction(key)
        print(self.myarray)

b=myhashexp()
b.addvaluefunction('1',100)
b.addvaluefunction('1',1000)
b.getthevalue('1')
