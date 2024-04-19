import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]
def horner(arr, n, x):

    # Initialize result
    result = arr[0]

    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, n):

        result = result*x + arr[i]

    return result

def rule(arr,m,x):
  if(m==0):
    return arr[0]
  return rule(arr,m-1,x)*x+arr[m]



list1=[]
list2=[]

def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=10 
x=3
while(n<=1000):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    rule(arr,n-1,x)
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(avg_time*1000)
  listy.append(n)
  list1.append(n)
  list2.append(n)
  n=n*2

plt.scatter(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
plt.scatter(list1,list2)
plt.xlabel("n")
plt.ylabel(" n ")
plt.show()

