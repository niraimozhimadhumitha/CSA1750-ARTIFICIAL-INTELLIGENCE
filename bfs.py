from collections import deque

# BFS function to traverse a graph
def bfs(graph, start_node):
    # Create a queue for BFS and enqueue the start node
    queue = deque([start_node])
    
    # Create a set to store visited nodes
    visited = set([start_node])

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()

        # Process the current node
        print(f"Visited node: {node}")

        # Get all adjacent nodes (neighbors) of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Enqueue the neighbor for future exploration

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS from a given start node
bfs(graph, 'A')
