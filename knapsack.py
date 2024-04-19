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

list1=[]
list2=[]
def greedy_knapsack(weights, profits, capacity):
    n = len(weights)
    ratios = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]
    ratios.sort(reverse=True)  

    max_profit = 0
    for _, w, p in ratios:
        if capacity >= w:
            max_profit += p
            capacity -= w
        else:
            max_profit += p * (capacity / w)
            break

    return max_profit







def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=10
capacity=500
while(n<=30):
  profits=random_generator(n)
  t_start= time.time()
  for i in range (10):
    weights=selection_sort(profits,n)
    x=profits/weights
    max_profit = greedy_knapsack( x, weights,capacity)
    print("Maximum achievable profit:", max_profit)

  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(avg_time*1000)
  listy.append(n)
  list1.append(n)
  list2.append(n*n)
  n=n+2

plt.plot(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
plt.scatter(list1,list2)
plt.xlabel("n")
plt.ylabel(" n sqaure")
plt.show()

