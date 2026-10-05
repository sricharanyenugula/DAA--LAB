# Kruskal's Algorithm in Python

# Find the parent of a vertex
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


# Join two sets
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


# Kruskal's Algorithm
def kruskal(vertices, edges):
    # Sort edges according to weight
    edges.sort(key=lambda x: x[2])

    parent = list(range(vertices))
    rank = [0] * vertices

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        # Add edge if it does not form a cycle
        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            union(parent, rank, u, v)

        # MST contains V-1 edges
        if len(mst) == vertices - 1:
            break

    return mst, total_cost


# -------------------------
# User Input
# -------------------------

vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []

print("\nEnter edges in the format: source destination weight")
print("Use vertex numbers from 0 to", vertices - 1)

for i in range(edges_count):
    u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v, weight))


# Run Kruskal's Algorithm
mst, total_cost = kruskal(vertices, edges)


# Display result
print("\nEdges in Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} = {weight}")

print("Total cost of Minimum Spanning Tree:", total_cost)