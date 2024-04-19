INF = 9999
def printSolution(numOfVertices, distance):
    for i in range(numOfVertices):
        for j in range(numOfVertices):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

def apsp(numOfVertices, G):
    distance = G
    for k in range(numOfVertices):
        for i in range(numOfVertices):
            for j in range(numOfVertices):
                distance[i][j] = min(
                    distance[i][j], distance[i][k]+distance[k][j])

    printSolution(numOfVertices, distance)


G = [[0, 8, INF, 1],
     [INF, 0, 1, INF],
     [4, INF, 0, INF],
     [INF, 2, 9, 1]
     ]

apsp(4, G)