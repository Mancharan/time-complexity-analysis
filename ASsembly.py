def assembly_line_scheduling(n, a11, a21, t1, t2, e1, e2, x1, x2):
    # Initialize arrays to store costs and line numbers
    f1 = [0] * (n + 1)
    f2 = [0] * (n + 1)
    L1 = [0] * (n + 1)
    L2 = [0] * (n + 1)

    # Initialize the special case when j = 1
    f1[1] = e1 + a11
    f2[1] = e2 + a21

    # Go through stations 2 to n
    for j in range(2, n + 1):
        # Check for smaller time for line 1
        if f1[j - 1] + a11 <= f2[j - 1] + t2[j - 1] + a11:
            # Previous station on line 1
            f1[j] = f1[j - 1] + a11
            L1[j] = 1
        else:
            # Previous station on line 2
            f1[j] = f2[j - 1] + t2[j - 1] + a11
            L1[j] = 2

        # Repeat the same for line 2
        # Check for smaller time for line 2
        if f2[j - 1] + a21 <= f1[j - 1] + t1[j - 1] + a21:
            # Previous station on line 2
            f2[j] = f2[j - 1] + a21
            L2[j] = 2
        else:
            # Previous station on line 1
            f2[j] = f1[j - 1] + t1[j - 1] + a21
            L2[j] = 1

    # Handle special case when j = n
    if f1[n] + x1 <= f2[n] + x2:
        F_star = f1[n] + x1
        L_star = 1
    else:
        F_star = f2[n] + x2
        L_star = 2

    # First print station (n) and the corresponding line number stored in L*
    print(f"Station {n} on Line {L_star}")

    # Go through stations from (n) down to (1)
    i = L_star
    for j in range(n, 1, -1):
        # Get line number
        i = L1[j] if i == 1 else L2[j]

        # Print station number (j-1)
        print(f"Station {j-1} on Line {i}")


# Example input values
n = 6
a11 = 4
a21 = 2
t1 = [2, 3, 1, 4, float('inf'), float('inf')]
t2 = [float('inf'), 2, 1, 3, float('inf'), float('inf')]
e1 = 3
e2 = 2
x1 = 2
x2 = 3

assembly_line_scheduling(n, a11, a21, t1, t2, e1, e2, x1, x2)