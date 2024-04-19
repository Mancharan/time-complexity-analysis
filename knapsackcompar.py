def knapsackpwr(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_profit = 0
    total_weight = 0
    knapsack_items = []

    for item in items:
        weight, profit = item
        if total_weight + weight <= capacity:
            knapsack_items.append(item)
            total_weight += weight
            total_profit += profit

    return total_profit, knapsack_items
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
def knapsackp(items, capacity):
    # Sort items based on profit in descending order
    items.sort(key=lambda x: x[1], reverse=True)

    total_profit = 0
    total_weight = 0
    knapsack_items = []

    for item in items:
        weight, profit = item
        if total_weight + weight <= capacity:
            knapsack_items.append(item)
            total_weight += weight
            total_profit += profit

    return total_profit, knapsack_items
import random

def generate_random_items(num_items, min_weight, max_weight, min_profit, max_profit):
    return [(random.randint(min_weight, max_weight), random.randint(min_profit, max_profit)) for _ in range(num_items)]

# Example usage
items = generate_random_items(10, 1, 10, 1, 20)
capacity = 10
max_profitp, selected_itemsp = knapsackp(items, capacity)


print("Maximum profit PROFIT SORTED:", max_profitp)
print("Items included in the knapsack:")
for item in selected_itemsp:
    print("Weight:", item[0], "Profit:", item[1])


max_profitpwr, selected_itemspwr = knapsackpwr(items, capacity)


print("Maximum profit PROFIT TO WIEGHT RATIO:", max_profitpwr)
print("Items included in the knapsack:")
for item in selected_itemspwr:
    print("Weight:", item[0], "Profit:", item[1])


max_profitw, selected_itemsw = knapsackw(items, capacity)

print("Maximum profit WEIGHT SORTED:", max_profitw)
print("Items included in the knapsack:")
for item in selected_itemsw:
    print("Weight:", item[0], "Profit:", item[1])



