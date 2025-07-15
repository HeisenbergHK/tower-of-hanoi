"""
Tower of Hanoi Puzzle Solver

This program solves the classic Tower of Hanoi puzzle using recursion.
The puzzle consists of three rods (A, B, C) and a number of disks of different sizes.
The goal is to move all disks from rod A to rod C, following these rules:
1. Only one disk can be moved at a time
2. Each move consists of taking the upper disk from one stack and placing it on top of another stack
3. No disk may be placed on top of a smaller disk

Time Complexity: O(2^n) where n is the number of disks
Space Complexity: O(n) due to the recursion stack
"""

# Initialize the three towers/rods as empty lists
A = []
B = []
C = []


def init(n):
    """
    Initialize tower A with n disks in decreasing order of size (largest at bottom).
    
    Args:
        n (int): Number of disks to place on tower A
        
    Returns:
        list: Tower A with n disks arranged in decreasing order of size
    """
    return [i for i in range(n, 0, -1)]  # Creates a list [n, n-1, ..., 1]


def solve(A, B, C, n):
    """
    Recursively solve the Tower of Hanoi puzzle.
    
    Args:
        A (list): Source tower/rod
        B (list): Auxiliary tower/rod
        C (list): Destination tower/rod
        n (int): Number of disks to move from A to C
        
    Algorithm:
        1. Move n-1 disks from A to B using C as auxiliary
        2. Move the largest disk from A to C
        3. Move n-1 disks from B to C using A as auxiliary
    """
    if n > 1:
        # Move n-1 disks from source to auxiliary
        solve(A, C, B, n - 1)
        
        # Move the largest disk from source to destination
        C.append(A.pop())
        
        # Move n-1 disks from auxiliary to destination
        solve(B, A, C, n - 1)
    else:
        # Base case: Move a single disk from source to destination
        C.append(A.pop())


def print_towers():
    """
    Print the current state of all three towers.
    """
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")


# Set the number of disks
N = 3

# Initialize tower A with N disks
A = init(N)

# Solve the Tower of Hanoi puzzle
solve(A, B, C, N)

# Print the final state of the towers
print_towers()