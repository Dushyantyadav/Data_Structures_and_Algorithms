class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

class mylinklist:
    def __init__(self):
            self.head=None

    def insertvalinfront(self,data):
        node=Node(data,self.head)
        self.head=node

    def myprinting(self):
        if self.head==None:
            print('Linked list empty')
            return
        itr=self.head
        mystr=''
        while itr:
            mystr=mystr+str(itr.data)+'--->'
            itr=itr.next
        print(mystr)
    def insertatend(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)
    def addlistfull(self,mylist):
        self.head=None
        for dd in mylist:
            self.insertatend(dd)

    def mylength(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count

    def removemyelement(self,ind):
        if ind<0 or ind>=self.mylength():
            raise Exception("Wrong Index")
        if ind==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:

            if count==ind-1:
                itr.next=itr.next.next

                break
            itr=itr.next
            count += 1

    def insertatfun(self,ind,value):
        if ind<0 or ind>=self.mylength():
            raise Exception("Wrong Index")
        if ind==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==ind-1:
                node=Node(value,itr.next)
                itr.next=node
                break
            itr=itr.next
            count=count+1

l1=mylinklist()
l1.addlistfull(['hello','mello','jello','pello'])
print(l1.mylength())
l1.myprinting()
l1.insertatfun(2,'JNL')
l1.myprinting()