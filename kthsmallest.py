import random
import time
import math
import matplotlib.pyplot as plt
listx=[]
listy=[]
arr=[]
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_select(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quick_select(arr, pivot_index + 1, high, k)
        else:
            return quick_select(arr, low, pivot_index - 1, k)

def find_kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None
    return quick_select(arr, 0, len(arr) - 1, k - 1)

# Example usage:
#arr = [7, 10, 4, 3, 20, 15]
#k = 3
#print("The", k, "th smallest element is:", find_kth_smallest(arr, k))
list1=[]
list2=[]

def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, 200))
  return arr

n=10
x_values=list()
y_values=list()
while(n<=500):
    arr=random_generator(n)

    start_time=time.time()
    for j in range(10):
       k=find_kth_smallest(arr,8)

    end_time=time.time()
    avg= (end_time-start_time)/10
    print(avg)
    x_values.append(avg*1000)
    y_values.append(n)
    list1.append(n)
    list2.append(n*n/10000)
    n=n+10
    print("hi")


print("end")

plt.scatter(y_values, x_values)

plt.xlabel('Average Time')
plt.ylabel('Array Size (n)')
plt.title('kth smallest Performance')
#plt.show('kth smallest_performance.png')  # Save the plot as an image
plt.plot(list1,list2)
plt.show()