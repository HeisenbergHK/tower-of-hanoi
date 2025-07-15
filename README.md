# Tower of Hanoi Solver

A Python implementation of the classic Tower of Hanoi puzzle using recursion.

## Description

The Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of different sizes. The puzzle starts with all disks stacked on one rod in order of decreasing size, with the smallest at the top.

The objective is to move the entire stack to another rod, following these rules:
1. Only one disk can be moved at a time
2. Each move consists of taking the upper disk from one stack and placing it on top of another stack
3. No disk may be placed on top of a smaller disk

This implementation uses a recursive algorithm to solve the puzzle efficiently.

## Features

- Solves the Tower of Hanoi puzzle for any number of disks
- Uses an elegant recursive approach
- Displays the final state of all three towers
- Well-documented code with detailed explanations

## Usage

```bash
python solver.py
```

By default, the program solves the puzzle for 3 disks. You can modify the `N` variable in the code to solve for a different number of disks.

## Algorithm

The recursive algorithm follows these steps:
1. Move n-1 disks from source to auxiliary rod
2. Move the largest disk from source to destination rod
3. Move n-1 disks from auxiliary to destination rod

## Complexity Analysis

- **Time Complexity**: O(2^n) where n is the number of disks
- **Space Complexity**: O(n) due to the recursion stack

## Example Output

For N = 3:
```
A: []
B: []
C: [3, 2, 1]
```

## License

This project is open source and available under the [MIT License](LICENSE).