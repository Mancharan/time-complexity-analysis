import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]
arr=list()
def selection_sort(arr,n):
    

    for i in range(n - 1):
       
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# A naive recursive implementation 
# of 0-1 Knapsack Problem 

# Returns the maximum value that 
# can be put in a knapsack of 
# capacity W 


def knapSack(W, wt, val, n): 

	# Base Case 
	if n == 0 or W == 0: 
		return 0

	# If weight of the nth item is 
	# more than Knapsack of capacity W, 
	# then this item cannot be included 
	# in the optimal solution 
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1) 

	# return the maximum of two cases: 
	# (1) nth item included 
	# (2) not included 
	else: 
		return max( 
			val[n-1] + knapSack( 
				W-wt[n-1], wt, val, n-1), 
			knapSack(W, wt, val, n-1)) 

# end of function knapSack 





# This code is contributed by Nikhil Kumar Singh 

def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=3
k=0
l= round(n/2)
#m=arr[l]
while(n<=250):
  W=50
  profit=random_generator(n)
  
  weight=random_generator(n)
  x=[]*n
  for i in range (n):
       x[i]=profit[i]/weight[i]
       pw= selection_sort(x)
  t_start= time.time()
  for i in range (10):
     print(knapSack(W,  pw,profit, n) )
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print("time: ",avg_time," for ",n," inputs")
  listx.append(avg_time)
  listy.append(n)
  #list1.append(n)
  #list2.append(n*n)
  n=n+10

plt.plot(listy,listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()
#plt.plot(list1,list2)
