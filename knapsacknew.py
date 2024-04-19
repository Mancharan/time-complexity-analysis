def knapsackw(weights_profits, capacity):
    n = len(weights_profits)
    # Initialize a table to store the maximum profit at each capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Building the dp table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights_profits[i - 1][0] <= w:
                dp[i][w] = max(dp[i - 1][w], weights_profits[i - 1][1] + dp[i - 1][w - weights_profits[i - 1][0]])
            else:
                dp[i][w] = dp[i - 1][w]

    # Tracing back to find the items included in the knapsack
    included_items = []
    total_profit = dp[n][capacity]
    remaining_capacity = capacity
    for i in range(n, 0, -1):
        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:
            included_items.append(i - 1)
            total_profit -= weights_profits[i - 1][1]
            remaining_capacity -= weights_profits[i - 1][0]

    return dp[n][capacity], included_items

import random

def generate_random_2d_array(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]





# Example usage
weights_profits = generate_random_2d_array(2,5,0,10)
capacity = 12
sorted_wp= sorted(weights_profits, key=lambda x: x[0])
print("Sorted 2D array based on the values of the first row:")
for row in sorted_wp:
    print(row)
max_profit, items = knapsack(sorted_wp, capacity)
print("Maximum profit:", max_profit)
print("Items included:", items)
