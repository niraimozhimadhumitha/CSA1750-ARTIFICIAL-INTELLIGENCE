from collections import deque

# Function to check if we can measure the target amount of water
def water_jug_solver(jug1_capacity, jug2_capacity, target_amount):
    # Check for impossible cases
    if target_amount > max(jug1_capacity, jug2_capacity):
        return "Not possible"
    
    # BFS queue to store the states (amount in jug1, amount in jug2)
    queue = deque()
    # Set to store visited states
    visited = set()

    # Start with both jugs empty
    queue.append((0, 0))

    # Perform BFS
    while queue:
        jug1, jug2 = queue.popleft()

        # If we reach the target amount in either jug
        if jug1 == target_amount or jug2 == target_amount:
            return f"Found solution: Jug1 = {jug1} liters, Jug2 = {jug2} liters"
        
        # If this state has already been visited, skip it
        if (jug1, jug2) in visited:
            continue

        # Mark this state as visited
        visited.add((jug1, jug2))

        # Possible moves
        possible_moves = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1))),  # Pour jug2 -> jug1
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug1 + jug2)),  # Pour jug1 -> jug2
        ]

        # Add all possible new states to the queue
        for new_jug1, new_jug2 in possible_moves:
            if (new_jug1, new_jug2) not in visited:
                queue.append((new_jug1, new_jug2))

    return "Not possible to measure the target amount"

# Example usage
jug1_capacity = 4  # Capacity of Jug 1 in liters
jug2_capacity = 3  # Capacity of Jug 2 in liters
target_amount = 2  # Target amount of water to measure

result = water_jug_solver(jug1_capacity, jug2_capacity, target_amount)
print(result)
