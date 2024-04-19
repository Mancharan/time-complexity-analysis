import random
import time
import matplotlib.pyplot as plt
def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    elif high == low + 1:
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])

    else:
        mid = (low + high) // 2

        # Divide the array into two halves and find max and min for each half
        max1, min1 = max_min(arr, low, mid)
        max2, min2 = max_min(arr, mid + 1, high)

        # Compare max and min of two halves
        max_val = max(max1, max2)
        min_val = min(min1, min2)

        return max_val, min_val

list1=[]
list2=[]
listx=[]
listy=[]
def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=10
while(n<=10000):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    max_min(arr,0,n-1)
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
