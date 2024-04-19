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
  




list1=[]
list2=[]

def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=100
while(n<=10000):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    horner(arr,n,3)
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(avg_time*1000)
  listy.append(n)
  list1.append(n)
  list2.append(n*n)
  n=n*2

plt.scatter(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
plt.scatter(list1,list2)
plt.xlabel("n")
plt.ylabel(" n sqaure")
plt.show()
