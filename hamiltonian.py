class Graph:
    def _init_(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def isSafe(self, v, pos, path, color):
        if self.graph[path[pos - 1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        if color[v] != -1:
            return False

        return True

    def hamCycleUtil(self, path, pos, color):
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(self.V):
            if self.isSafe(v, pos, path, color):
                path[pos] = v
                color[v] = pos

                if self.hamCycleUtil(path, pos + 1, color):
                    return True

                path[pos] = -1
                color[v] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V
        color = [-1] * self.V

        path[0] = 0
        color[0] = 0

        if not self.hamCycleUtil(path, 1, color):
            print("Hamiltonian cycle does not exist")
            return False

        print("Hamiltonian cycle exists:")
        self.printSolution(path)
        return True

    def printSolution(self, path):
        for vertex in path:
            print(vertex, end=" ")
        print(path[0])

# Example usage:
g = Graph(5)
g.graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

g.hamCycle()