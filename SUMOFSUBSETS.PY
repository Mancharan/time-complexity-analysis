def subset_sum(nums, target):
    result = []

    def backtrack(current_subset, index):
        if sum(current_subset) == target:
            result.append(current_subset[:])
            return
        if sum(current_subset) > target or index >= len(nums):
            return

        # Include nums[index] in the current subset
        backtrack(current_subset + [nums[index]], index + 1)

        # Exclude nums[index] from the current subset
        backtrack(current_subset, index + 1)

    backtrack([], 0)
    return result

# Example usage:
nums = [2, 4, 6, 8]
target = 10
subsets = subset_sum(nums, target)
if subsets:
    print("Subsets with sum equal to", target, "are:")
    for subset in subsets:
        print(subset)
else:
    print("No subset found with sum equal to", target)
