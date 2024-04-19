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

def hanoi(n, f, to, via):
    count=12
    if n == 1:
       count=count+1
       #print("Move disk 1 from",f,"to",to);
    else:
        hanoi(n-1, f, via, to)
        print("Move disk",n,"from",f,"to",to);
        hanoi(n-1, via, to, f)


def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=3
while(n<=7):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    hanoi(n,'a','b','c')
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print(avg_time, n)
  listx.append(avg_time*1000)
  listy.append(n)
  n=n+1

plt.scatter(listy,listx)
plt.show()
