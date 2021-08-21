class mybintree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def addval(self,data):
        if self.data==data:
            return
        if data<self.data:
            if self.left:
                self.left.addval(data)
            else:
                self.left=mybintree(data)
        if data>self.data:
            if self.right:
                self.right.addval(data)
            else:
                self.right=mybintree(data)
    def inordtrav(self):
        mylst=[]
        if self.left:
            mylst+=self.left.inordtrav()
        
        mylst.append(self.data)

        if self.right:
            mylst+=self.right.inordtrav()
        return mylst
    
    def postordertravl(self):
        mylst1=[]

        if self.left:
            mylst1+=self.left.postordertravl()
        if self.right:
            mylst1+=self.right.postordertravl()
        
        mylst1.append(self.data)

        return mylst1
    
    def findmaxele(self):
        if self.right is None:
            return self.data
        return self.right.findmaxele()
    
    def myminele(self):
        if self.left:
            return self.left.myminele()
        return self.data
    
    def mysum(self):
        leftsum=self.left.mysum() if self.left else 0
        rightsum=self.right.mysum() if self.right else 0

        return self.data+leftsum+rightsum

    def preordertrav(self):
        mylst2=[]

        mylst2.append(self.data)

        if self.left:
            mylst2+=self.left.preordertrav()
        if self.right:
            mylst2+=self.right.preordertrav()
        
        return mylst2

    def srchval(self,val):
        if val==self.data:
            return True

        if val<self.data:
            if self.left:
                return self.left.inordtrav(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.srchval(val)
            else:
                return False

def crtbintree(elelst):
    root=mybintree(elelst[0])
    for i in range(1,len(elelst)):
        root.addval(elelst[i])
    return root

if __name__=='__main__':
    
    ex=[1,34,2]
    mytree1=crtbintree(ex)
    print(mytree1.mysum())