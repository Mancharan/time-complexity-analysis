import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]
arr=[]
n=int(input("enter "))
def magicsq(n):

    magicsq = [[0] * n for _ in range(n)]

    row = 0
    col = n // 2

    magicsq[row][col] = 1

    for x in range(2, n * n + 1):
        r, c = row - 1, col - 1
        if r < 0:
            r += n

        if c < 0:
            c += n

        if magicsq[r][c] > 0:
            row += 1
            if row >= n:
                row -= n
        else:
            row = r
            col = c
        magicsq[row][col] = x

    for i in range(n):
        for j in range(n):
            print(magicsq[i][j], end=" ")
        print()


# Example usage






list1=[]
list2=[]

def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, 20))
  return arr


x_values=list()
y_values=list()
t=n
while t <50:
    start_time=time.time()
    for j in range(10):


        magicsq(t)

    end_time=time.time()
    avg= (end_time-start_time)/10
    print(avg)
    x_values.append(avg)
    y_values.append(t)
    t+=2
print("hi")


print("en")

plt.scatter(y_values, x_values)
plt.xlabel('Average Time')
plt.ylabel('Array Size (n)')
plt.title('magic square Performance')
plt.show()  # Save the plot as an image