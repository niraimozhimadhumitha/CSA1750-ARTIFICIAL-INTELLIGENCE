import itertools

# Function to solve the cryptarithmetic problem
def cryptarithmetic_solver():
    # The letters involved in the equation
    letters = 'SENDMORY'
    
    # Generate all possible digit permutations for the letters
    for perm in itertools.permutations(range(10), len(letters)):
        # Create a dictionary to map each letter to a digit
        mapping = dict(zip(letters, perm))

        # Extract the numbers from the current mapping
        send = mapping['S']*1000 + mapping['E']*100 + mapping['N']*10 + mapping['D']
        more = mapping['M']*1000 + mapping['O']*100 + mapping['R']*10 + mapping['E']
        money = mapping['M']*10000 + mapping['O']*1000 + mapping['N']*100 + mapping['E']*10 + mapping['Y']

        # Check if the equation SEND + MORE = MONEY holds true
        if send + more == money and mapping['S'] != 0 and mapping['M'] != 0:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print(f"Mapping: {mapping}")
            return  # Stop after finding the first solution

    print("No solution found")

# Run the solver
cryptarithmetic_solver()
