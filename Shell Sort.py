def myshellsort(arr):

    mysz=len(arr)
    gp=mysz//2
    while gp>0:
        for i in range(gp,mysz):
            anc=arr[i]
            j=i
            while j>=gp and anc<arr[j-gp]:
                arr[j]=arr[j-gp]
                j=j-gp
            arr[j]=anc
        gp=gp//2
    return arr

if __name__=='__main__':
    c=myshellsort([2,12,45,23,13,24,52,1,4,5,79])
    print(c)