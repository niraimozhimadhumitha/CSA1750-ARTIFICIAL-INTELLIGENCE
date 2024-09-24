import heapq

# Function to calculate the Manhattan distance
def manhattan_distance(start, goal):
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(start.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Function to check if the puzzle is solvable
def is_solvable(puzzle):
    inv_count = 0
    puzzle = [i for i in puzzle if i != 0]
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j]:
                inv_count += 1
    return inv_count % 2 == 0

# Class to represent a puzzle state
class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # Heuristic function (Manhattan distance)
    def manhattan(self):
        return manhattan_distance(self.board, self.goal)

    # Total cost: moves made + heuristic
    def cost(self):
        return self.moves + self.manhattan()

    # Check if this is the goal state
    def is_goal(self):
        return self.board == self.goal

    # Get possible neighbor states
    def neighbors(self):
        neighbors = []
        zero_pos = self.board.index(0)
        x, y = divmod(zero_pos, 3)

        # Define possible moves (left, right, up, down)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_pos = nx * 3 + ny
                new_board = self.board[:]
                new_board[zero_pos], new_board[new_pos] = new_board[new_pos], new_board[zero_pos]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    # Define comparison for priority queue (based on cost)
    def __lt__(self, other):
        return self.cost() < other.cost()

# A* algorithm to solve the puzzle
def a_star_solver(initial_board):
    if not is_solvable(initial_board):
        return None  # Puzzle is not solvable

    # Priority queue for the A* algorithm
    open_set = []
    heapq.heappush(open_set, PuzzleState(initial_board))

    # Set of explored states
    explored = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return current_state

        explored.add(tuple(current_state.board))

        for neighbor in current_state.neighbors():
            if tuple(neighbor.board) not in explored:
                heapq.heappush(open_set, neighbor)

    return None

# Function to reconstruct the solution path
def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    return path[::-1]

# Example usage:
initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # Example puzzle configuration

solution = a_star_solver(initial_board)

if solution:
    print("Puzzle solved!")
    path = reconstruct_path(solution)
    for step in path:
        print(step)
else:
    print("Puzzle is not solvable.")
