import time
a=[]
for j in range (0,1000000):
	a.append('nemo')
print(len(a))
def find_my_arr(a):
	st=time.time()
	for i in range(0,len(a)):
		if a[i]=='nemo':
			print('Word found')
		else:
			print('word not found')
	print('It took',time.time()-st,'milliseconds')

find_my_arr(a)