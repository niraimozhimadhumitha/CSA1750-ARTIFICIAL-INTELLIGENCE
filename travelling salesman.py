import itertools

# Function to calculate the total distance of a given tour
def calculate_tour_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Return to the starting city
    return total_distance

# Function to solve the TSP using brute-force
def traveling_salesman_bruteforce(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    
    # Generate all possible tours
    all_tours = itertools.permutations(cities)
    
    # Initialize the best tour and minimum distance
    best_tour = None
    min_distance = float('inf')
    
    # Check each tour
    for tour in all_tours:
        current_distance = calculate_tour_distance(tour, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = tour
    
    return best_tour, min_distance

# Example distance matrix (symmetric)
# distance_matrix[i][j] represents the distance between city i and city j
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Find the best tour and minimum distance
best_tour, min_distance = traveling_salesman_bruteforce(distance_matrix)

# Print the result
print("Best tour:", best_tour)
print("Minimum distance:", min_distance)
