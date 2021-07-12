def myfibonacci(n,arr):
    for i in range(n):
        c=arr[i]+arr[i+1]
        arr.append(c)
    return arr

if __name__=='__main__':
    p=[0,1]
    x=myfibonacci(20,p)
    print(x)