from collections import deque

# Function to check if a state is valid
def is_valid_state(state):
    m_left, c_left, boat, m_right, c_right = state
    
    # Condition to check that cannibals do not outnumber missionaries on either side
    if (m_left >= 0 and c_left >= 0 and m_right >= 0 and c_right >= 0 and
        (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right)):
        return True
    return False

# Function to check if a state is the goal state (all people are on the right side)
def is_goal_state(state):
    _, _, boat, m_right, c_right = state
    return m_right == 3 and c_right == 3 and boat == 1

# Function to generate all possible moves from the current state
def get_successors(state):
    m_left, c_left, boat, m_right, c_right = state
    successors = []
    
    # Possible moves: (1 missionary, 0 cannibals), (2 missionaries, 0 cannibals),
    # (0 missionaries, 1 cannibal), (0 missionaries, 2 cannibals), (1 missionary, 1 cannibal)
    if boat == 0:  # If the boat is on the left side
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m_left - m, c_left - c, 1, m_right + m, c_right + c)
            if is_valid_state(new_state):
                successors.append(new_state)
    else:  # If the boat is on the right side
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m_left + m, c_left + c, 0, m_right - m, c_right - c)
            if is_valid_state(new_state):
                successors.append(new_state)

    return successors

# BFS algorithm to find the solution
def cannibals_missionaries():
    # Initial state: (3 missionaries on left, 3 cannibals on left, boat on left (0), 0 missionaries on right, 0 cannibals on right)
    start_state = (3, 3, 0, 0, 0)
    
    # Queue for BFS
    queue = deque([start_state])
    # Set to keep track of visited states
    visited = set([start_state])
    # Dictionary to keep track of the path (for backtracking)
    parent = {start_state: None}
    
    while queue:
        current_state = queue.popleft()

        # If we reach the goal state, reconstruct the path
        if is_goal_state(current_state):
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent[current_state]
            return path[::-1]  # Return the path in reverse (from start to goal)
        
        # Explore all successors of the current state
        for next_state in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
                parent[next_state] = current_state  # Keep track of how we reached this state
    
    return None  # No solution found

# Function to print the solution
def print_solution(path):
    if path:
        print("Solution found in {} moves:".format(len(path) - 1))
        for step, state in enumerate(path):
            m_left, c_left, boat, m_right, c_right = state
            side = "left" if boat == 0 else "right"
            print(f"Step {step}:")
            print(f"  Left bank: {m_left} missionaries, {c_left} cannibals")
            print(f"  Right bank: {m_right} missionaries, {c_right} cannibals")
            print(f"  Boat is on the {side} side")
            print()
    else:
        print("No solution found.")

# Find the solution
solution_path = cannibals_missionaries()

# Print the solution
print_solution(solution_path)
