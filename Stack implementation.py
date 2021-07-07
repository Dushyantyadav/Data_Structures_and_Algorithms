from collections import deque
mystack=deque()
mystack.append('Hello')
mystack.append('Good Morning')
mystack.append('Bye')
mystack.append('Hi')
mystack.append('Whatever')

print(mystack)

mylist=[]
mylist.append('Hello')
mylist.append('Good Morning')
mylist.append('Bye')
mylist.append('Hi')
mylist.append('Whatever')
print(mylist)
print(mylist.pop())
print(mylist.pop())

class mystackclass:
    def __init__(self):
        self.storing=deque()
    def addelement(self,element):
        self.storing.append(element)
    def removeelement(self):
        self.storing.pop()
    def printmyelement(self):
        print(self.storing[-1])
    def printallstack(self):
        print(self.storing)

dog=mystackclass()
dog.addelement('Raju')
dog.addelement('Shyam')
dog.addelement('Babu Rao')
dog.printmyelement()
dog.printallstack()
dog.removeelement()
dog.printallstack()