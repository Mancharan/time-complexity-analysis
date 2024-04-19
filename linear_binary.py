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
def LinearSearch(arr, size, key):

    # If the array is empty we will return -1
    if (size == 0):
        return -1

    elif (arr[size - 1] == key):

        # Return the index of found key.
        return size - 1

    return LinearSearch(arr, size - 1, key)
def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
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
while(n<=1000):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    LinearSearch(arr,n,99999)
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(avg_time*10000)
  listy.append(n)
  list1.append(n)
  list2.append(n*n)
  n=n*2

plt.plot(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
plt.plot(list1,list2)
plt.xlabel("n")
plt.ylabel(" n sqaure")
plt.show()

