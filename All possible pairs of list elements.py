a=[x for x in input('Enter elements of Array').split()]

def allpospair(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            print(a[i],a[j])

allpospair(a)
print(type(a))