import time
import matplotlib.pyplot as plt

def min_cost(adj_matrix):
    n = len(adj_matrix)
    cost = [0] * n
    path = [-1] * n

    for i in range(n - 2):
        min_cost = float('inf')
        min_j = -1
        for j in range(n):
            if adj_matrix[i][j] != float('inf') and adj_matrix[i][j] + cost[j] < min_cost:
                min_cost = adj_matrix[i][j] + cost[j]
                min_j = j
        cost[i] = min_cost
        path[i] = min_j

    return cost, path

def print_stages(adj_matrix):
    n = len(adj_matrix)
    cost, path = min_cost(adj_matrix)
    stages = []
    i = 0
    while i != -1:
        stages.append(i)
        i = path[i]

    print("The stages of the multistage graph are:")
    print(" -> ".join(map(str, stages)))

def time_complexity_plot():
    input_sizes = []
    execution_times = []

    for n in range(10, 100, 10):  # Varying input size from 10 to 100
        adj_matrix = [[float('inf')] * n for _ in range(n)]  # Generating adjacency matrix of size n x n
        start_time = time.time()
        print_stages(adj_matrix)
        execution_time = time.time() - start_time
        input_sizes.append(n)
        execution_times.append(execution_time)
     

    # Plotting
    plt.plot(input_sizes, execution_times, marker='o')
    plt.title("Time Complexity of min_cost function")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.show()

