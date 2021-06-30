class hop:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('My name is {} and my age is {}'.format(name,age))
    def updtdy(self):
        self.age=100
    def compare(self,other):
        if self.age==other.age:
            print('The ages are same')
        else:
            print('They have different age')

a1=hop('Dushyant',23)
a2=hop('Ram',23)

a1.updtdy()
a1.compare(a2)






