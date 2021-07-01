#Hash table

class mytesting:
    def __init__(self):
        self.mymax=10
        self.myarr=[None for i in range(0,self.mymax)]

    def my_hash_func(self,key):
        h=0
        for al in key:
            h=h+ord(al)
        return h%10
    def my_add(self,key,value):
        h=self.my_hash_func(key)
        self.myarr[h]=value

    def my_getval(self,key):
        h=self.my_hash_func(key)
        print(self.myarr[h])

a1=mytesting()
a1.my_add('March 11',1100)
a1.my_getval('March 11')