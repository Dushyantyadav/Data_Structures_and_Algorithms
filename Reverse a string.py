a=input('Enter your string')
b=[]
c=[]

def reversemystring():
    for i in a:
        b.append(i)
    for l in range(0,len(b)):
        c.append(a[len(b)-l-1])
    strss=''
    for j in c:
        strss=strss+j
    print(strss)

reversemystring()
