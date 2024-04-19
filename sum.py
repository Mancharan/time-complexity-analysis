import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]

def sum(arr, b):
 if(n==1):
  return arr[0]
 else:
  return(arr[b]+sum(arr,b-1))


list1=[]
list2=[]

def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=10
while(n<=100):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    b=n-1
    sum1= sum(arr,b)
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(avg_time*1000)
  listy.append(n)
  list1.append(n)
  list2.append(n*n)
  n=n*10

plt.scatter(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
plt.scatter(list1,list2)
plt.xlabel("n")
plt.ylabel(" n sqaure")
plt.show()

