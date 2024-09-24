# Function for DFS traversal
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()  # To keep track of visited nodes

    visited.add(start_node)
    print(f"Visited node: {start_node}")

    # Recur for all the adjacent nodes that haven't been visited yet
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run DFS starting from node 'A'
dfs(graph, 'A')
