import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]
def selection_sort(arr, n):
  for ind in range(n):
    min=ind
    for j in range(ind+1,n):
       if arr[j] < arr[min]:
                min = j
         # swapping the elements to sort the array
                (arr[ind], arr[min]) = (arr[min], arr[ind])
  return arr
def LinearSearch(arr, size, key):

    # If the array is empty we will return -1
    if (size == 0):
        return -1

    elif (arr[size - 1] == key):

        # Return the index of found key.
        return size - 1

    return LinearSearch(arr, size - 1, key)
def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=100
k=0
l= round(n/2)
m=10001
while(n<=1000):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    LinearSearch(arr,n,999999)
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(round(avg_time*10000))
  listy.append(n)
  
  n=n*2

plt.scatter(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
