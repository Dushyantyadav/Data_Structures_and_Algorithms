class inssort:
    def mysrtfun(self,arr):
        for i in range(1,len(arr)):
            stay=arr[i]
            j=i-1
            while j>=0 and stay<arr[j]:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=stay
        print(arr)

if __name__=='__main__':
    a=inssort()
    a.mysrtfun([1,7,3,8,12,15,21,2,4])