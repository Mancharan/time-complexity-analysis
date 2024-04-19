import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]



def partition(arr,l,h):
	i = ( l - 1 )
	x = arr[h]

	for j in range(l , h):
		if arr[j] <= x:

			# increment index of smaller element
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[h] = arr[h],arr[i+1]
	return (i+1)


def quickSortIterative(arr,l,h):

	# Create an auxiliary stack
	size = h - l + 1
	stack = [0] * (size)

	# initialize top of stack
	top = -1


	top = top + 1
	stack[top] = l

	top = top + 1
	stack[top] = h


	while top >= 0:

		# Pop h and l
		h = stack[top]
		top = top - 1
		l = stack[top]
		top = top - 1

		p = partition( arr, l, h )


		if p-1 > l:
			top = top + 1
			stack[top] = l
			top = top + 1
			stack[top] = p - 1

		if p+1 < h:
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h





list1=[]
list2=[]

def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=10
k=0
l= round(n/2)

while(n<=100000):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
     quickSortIterative(arr,0,n-1)

  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append((avg_time*10))
  listy.append(n)
  list1.append(n)
  list2.append(n)
  n=n*5

plt.scatter(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
plt.plot(list1,list2)
plt.xlabel("n")
plt.ylabel(" n sqaure")
plt.show()

