class myfirsttree:
    def __init__(self,fv):
        self.fv=fv
        self.child=[]
        self.par= None

    def addchildval(self,val):
        val.par=self
        self.child.append(val)

    def printmytree(self):
        print(self.fv)
        if self.child:
            for val in self.child:
                val.printmytree()

def buildmytree():

    r1=myfirsttree("Gadgets")

    r2=myfirsttree("Laptop")
    r2.addchildval(myfirsttree("Mac"))
    r2.addchildval(myfirsttree("Windows"))
    r2.addchildval(myfirsttree("Dell"))

    r3=myfirsttree("Mobile")
    r3.addchildval(myfirsttree("Nokia"))
    r3.addchildval(myfirsttree("Apple"))
    r3.addchildval(myfirsttree("Samsung"))

    r4=myfirsttree("TV")
    r4.addchildval(myfirsttree("Sony"))
    r4.addchildval(myfirsttree("LG"))
    r4.addchildval(myfirsttree("Panasonic"))

    r1.addchildval(r2)
    r1.addchildval(r3)
    r1.addchildval(r4)

    return r1


if __name__=='__main__':
    r1= buildmytree()
    r1.printmytree()
    pass