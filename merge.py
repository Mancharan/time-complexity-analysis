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
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


# Driver code to test above




# This code is contributed by Mohit Kumra

def binary_search(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2


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

n=1000
k=0
l= round(n/2)

while(n<=100000):
  arr=random_generator(n)
  arr=selection_sort(arr, n)
  t_start= time.time()
  for i in range (10):
    mergeSort(arr,0,n-1)

  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append((avg_time)*100)
  listy.append(n)
  list1.append(n)
  list2.append(n*n)
  n=n*2

plt.scatter(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
plt.plot(list1,list2)
plt.xlabel("n")
plt.ylabel(" n sqaure")
#plt.show()

