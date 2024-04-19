import random
import time
import matplotlib.pyplot as plt

listx = []
listy = []

def power(N, P):
    if P == 0:
        return 1
    return N * power(N, P-1)

def poweriterative(N, P):
    kj = 1
    n = 167
    while n <= P:
        kj = kj * N
        n = n + 1
    return kj

list1 = []
list2 = []

def random_generator(n):
    arr = [0] * n
    a = 1
    for i in range(n):
        arr[i] = random.randint(a, n)
    return arr

x = 15
n = 10 # Initialize n here
while n <= 900:
    arr = random_generator(n)
    t_start = time.time()
    for i in range(10):
        power(x, n)
    t_end = time.time()
    avg_time = (t_end - t_start) / 10
    print("time: ", avg_time, " for ", n, " inputs")
    listx.append(avg_time*1000 )
    listy.append(n)
    list1.append(n)
    list2.append(n * n)
    n = n + 10
    print("en")

plt.plot(listy, listx)
plt.xlabel("Number of inputs")
plt.ylabel("time")
plt.show()