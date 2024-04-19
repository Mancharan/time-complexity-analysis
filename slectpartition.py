import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]
def partition(arr, start, end):
    pivot_index = start
    pivot_value = arr[end]  # Choosing the last element as pivot
    for i in range(start, end):
        if arr[i] < pivot_value:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return pivot_index

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = partition(arr, i, n - 1)
        arr[i], arr[min_index] = arr[min_index], arr[i]




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
    selection_sort(arr)
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
