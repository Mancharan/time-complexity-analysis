def knapsack(weights, profits, capacity):
    n = len(weights)
    # Initialize a dictionary to store the maximum profit for each subset of items
    dp = {}
    dp[frozenset()] = 0  # Base case: no items have been selected yet

    # Build the dp dictionary
    for i in range(n):
        # Create a new dictionary to store the updated values of dp
        new_dp = dp.copy()
        for subset, max_profit in dp.items():
            # Add the current item to the subset if it doesn't exceed the capacity
            if sum(weights[item] for item in subset) + weights[i] <= capacity:
                new_subset = subset.union({i})
                new_profit = max_profit + profits[i]
                # Update the maximum profit for the new subset
                if new_subset not in new_dp or new_profit > new_dp[new_subset]:
                    new_dp[new_subset] = new_profit
        # Update dp with the new values
        dp.update(new_dp)

    # Find the subset with the maximum profit
    max_profit = max(dp.values())
    max_subset = max(dp, key=dp.get)

    return max_profit, max_subset

# Example usage:
weights = [10, 20, 30,45,73]  # Weights of items
profits = [60, 100, 120,33,124]  # Profits of items
capacity = 100
max_profit, max_subset = knapsack(weights, profits, capacity)
print("Maximum profit:", max_profit)
print("Items included in knapsack:", max_subset)
