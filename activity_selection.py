import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]

def printMaxActivities(s, f ):
	n = len(f)
    

	# The first activity is always selected
	i = 0
	print(i)

	# Consider rest of the activities
	for j in range(n):

		# If this activity has start time greater than
		# or equal to the finish time of previously
		# selected activity, then select it
		if s[j] >= f[i]:
			print(j)
			i = j

# Driver program to test above function


def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=10
k=0
while(n<=10):
  s=random_generator(n)
  f=random_generator(n)
  
  t_start= time.time()
  for i in range (10):
   printMaxActivities(s, f)
   print("selected")
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(avg_time*10000)
  listy.append(n)
 
  n=n*2

plt.plot(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()



# This code is contributed by Nikhil Kumar Singh
