import random

def generate_random_items(num_items, min_weight, max_weight, min_profit, max_profit):
    return [(random.randint(min_weight, max_weight), random.randint(min_profit, max_profit)) for _ in range(num_items)]

# Example usage
items = generate_random_items(5, 1, 10, 1, 20)
capacity = 10

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

max_profit, selected_items = knapsack(items, capacity)

print("Maximum profit:", max_profit)
print("Items included in the knapsack:")
for item in selected_items:
    print("Weight:", item[0], "Profit:", item[1])
