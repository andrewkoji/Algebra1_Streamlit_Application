import random
import numpy as np

def XY_solution():
    """Generate a random equation ax + by = c and ensure there is always a valid (x, y) pair that satisfies it."""
    # Generate random coefficients for the equation
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    # Ensure a and b are not both zero to avoid a degenerate equation
    while a == 0 and b == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    # Randomly choose a valid (x, y) pair
    x = random.randint(-25, 25)
    y = random.randint(-25, 25)

    # Calculate c to ensure the equation is satisfied
    c = a * x + b * y

    # Find all valid (x, y) pairs
    valid_pairs = []
    for x_candidate in range(-25, 26):  # Iterate through possible values of x
        for y_candidate in range(-25, 26):  # Iterate through possible values of y
            if a * x_candidate + b * y_candidate == c:  # Check if the equation is satisfied
                valid_pairs.append((x_candidate, y_candidate))  # Add the valid pair to the list

    # Select a random solution from the valid pairs
    solution = random.choice(valid_pairs)
    result = {
        "equation": f"{f'{a}x ' if a != 0 else ''}{f'+ {b}y ' if b > 0 else f'- {-b}y ' if b < 0 else ''}= {c}".strip(),
        "solution": solution,
        "verification": f"{a}({solution[0]}) + {b}({solution[1]}) = {c}"
    }

    return result

# Generate a random equation and find a solution
result = XY_solution()
print("Equation:", result["equation"])
print("Solution:", result["solution"])
print("Verification:", result["verification"])