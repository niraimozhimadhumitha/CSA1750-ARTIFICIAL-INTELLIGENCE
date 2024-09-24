# Function to check if a queen can be placed at board[row][col]
def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

# Function to solve the N-Queens problem using backtracking
def solve_n_queens(board, row):
    if row == len(board):
        # If all queens are placed, return the solution
        return True
    
    # Try placing a queen in all columns in the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            if solve_n_queens(board, row + 1):
                return True

            # Backtrack and remove the queen from the current cell
            board[row][col] = 0

    return False

# Function to print a single solution
def print_solution(board):
    for row in board:
        print(" ".join('Q' if col == 1 else '.' for col in row))
    print()

# Function to initialize the board and start solving process
def solve():
    n = 8  # Size of the board (8x8)
    board = [[0 for _ in range(n)] for _ in range(n)]  # Initialize an empty board
    
    # If a solution exists, print it
    if solve_n_queens(board, 0):
        print_solution(board)
    else:
        print("No solution exists")

# Start the solver
solve()
