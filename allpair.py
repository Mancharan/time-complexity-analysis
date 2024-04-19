def print_path(paths, i, j):
    if paths[i][j] == float('inf'):
        print(f"No path from {i} to {j}")
        return
    path = [i]
    while i != j:
        i = paths[i][j]
        path.append(i)
    print("Path from", path[0], "to", path[-1], ":", "->".join(map(str, path)))

def floyd_warshall(graph):
    n = len(graph)
    # Initialize paths matrix with initial paths and distances
    paths = [[j if i != j and graph[i][j] != float('inf') else None for j in range(n)] for i in range(n)]

    # Calculate shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    paths[i][j] = paths[k][j]

    # Print paths
    for i in range(n):
        for j in range(n):
            if i != j:
                print_path(paths, i, j)

# Example graph represented as an adjacency matrix
graph = [
    [0, 3, 0, 7],
    [8, 0, 2, 1],
    [5, 5, 0, 1],
    [2, 7, 2, 0]
]

# Applying Floyd-Warshall algorithm
floyd_warshall(graph)
