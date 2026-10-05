from collections import deque

# Create graph
graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for i in range(e):
    u, v = map(int, input().split())

    # Undirected graph
    graph[u].append(v)
    graph[v].append(u)


# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# DFS
def dfs(graph, start):
    visited = set()
    result = []

    def dfs_recursive(vertex):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return result


# Display graph
print("\nGraph:")
for vertex in graph:
    print(vertex, "->", graph[vertex])


# Starting vertex
start = int(input("\nEnter starting vertex: "))

# Perform BFS and DFS
print("\nBFS Traversal:", bfs(graph, start))
print("DFS Traversal:", dfs(graph, start))