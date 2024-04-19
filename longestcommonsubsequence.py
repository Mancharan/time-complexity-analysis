def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Initialize a table to store lengths of LCSs
    # dp[i][j] will store the length of LCS of X[0...i-1] and Y[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS itself
    lcs_length = dp[m][n]
    lcs = [""] * lcs_length

    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


# Example usage:
X = input("Enter the first string: ")
Y = input("Enter the second string: ")
print("Longest Common Subsequence:", longest_common_subsequence(X, Y))
