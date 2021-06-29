x=[i for i in input("Enter the first array").split()]
y=[j for j in input("Enter the first array").split()]

flag=0
for k in range(0,len(x)):
    for l in range(0,len(y)):
        if x[k]==y[l]:
            flag=1
        else:
            continue

if flag==1:
    print("Arrays have a common element")
else:
    print('No common element found')