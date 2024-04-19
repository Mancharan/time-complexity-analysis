import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]


def bool(k,n):
  if(k==n):
    #print("newwww")
    i=0
    for i in range(n):
      print(x[i],end=" ")
  else:
    x[k]=True
    bool(k+1,n)
    x[k]=False
    bool(k+1,n)





list1=[]
list2=[]

def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=2
k=0
x=[True]*(n+1)
while(n<=7):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    bool(k,n)
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(avg_time*1000)
  listy.append(n)
  list1.append(n)
  list2.append(n*n)
  n=n+1
x=[True]*(n+1)
plt.scatter(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
plt.scatter(list1,list2)
plt.xlabel("n")
plt.ylabel(" n sqaure")
plt.show()

