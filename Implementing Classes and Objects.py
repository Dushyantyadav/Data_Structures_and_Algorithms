class dushyant:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('This statement always prints')
    def hello(self):
        print('Hello Everyone',self.a,self.b)


a1=dushyant(22,11)
a2=dushyant(124124,2412412)
dushyant.hello(a1)
dushyant.hello(a2)
