# Prim's Algorithm in Python

INF = 999999

# Number of vertices
n = int(input("Enter number of vertices: "))

# Create adjacency matrix
graph = []

print("Enter the adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Arrays
selected = [False] * n
selected[0] = True

print("\nEdges in Minimum Spanning Tree:")

total_cost = 0

# MST contains n-1 edges
for _ in range(n - 1):
    minimum = INF
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {graph[x][y]}")

    total_cost += graph[x][y]
    selected[y] = True

print("\nTotal cost of Minimum Spanning Tree:", total_cost)