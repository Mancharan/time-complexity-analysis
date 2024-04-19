import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]
def selection_sort(arr, n):
  for ind in range(n):
    min=ind;
    for j in range(ind+1,n):
       if arr[j] < arr[min]:
                min = j
         # swapping the elements to sort the array
                (arr[ind], arr[min]) = (arr[min], arr[ind])
  return arr
def binary_search(arr, low, high, x):

    if high >= low:

        mid = round((high + low) // 2)


        if arr[mid] == x:
            return mid


        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)


        else:
            return binary_search(arr, mid + 1, high, x)

    else:

        return -1




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
m=10001
while(n<=1000):
 
  arr=random_generator(n)
  arr=selection_sort(arr,n) 
  t_start= time.time()
  for i in range (10):
    binary_search(arr,k,n-1,m)
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append((avg_time*10))
  listy.append(n)
  list1.append(n)
  list2.append(n*n)
  n=n*2

plt.scatter(listx,listy)
plt.ylabel("Number of inputs")
plt.xlabel("time")
plt.show()



