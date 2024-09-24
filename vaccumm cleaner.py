from collections import deque

# Function to check if a position is within bounds of the grid
def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

# Function to clean the grid using BFS
def vacuum_cleaner(grid, start):
    rows, cols = len(grid), len(grid[0])
    
    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Queue for BFS
    queue = deque([start])
    
    # Set to keep track of visited positions
    visited = set([start])
    
    # BFS to clean the grid
    while queue:
        x, y = queue.popleft()

        # Clean the current position
        if grid[x][y] == 1:  # If the cell is dirty (1), clean it (set it to 0)
            print(f"Cleaning dirt at position ({x}, {y})")
            grid[x][y] = 0

        # Explore all 4 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    # Return the final cleaned grid
    return grid

# Example grid (0 = clean, 1 = dirty)
grid = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]

# Starting position of the vacuum cleaner
start_position = (0, 0)

# Clean the grid
final_grid = vacuum_cleaner(grid, start_position)

# Print the final grid after cleaning
print("Final cleaned grid:")
for row in final_grid:
    print(row)
