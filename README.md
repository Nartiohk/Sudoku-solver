# Sudoku Solver (Python - Backtracking)

## Overview

This is a Python-based Sudoku solver that uses the Backtracking Algorithm to efficiently solve 9x9 Sudoku puzzles. The algorithm recursively attempts to place numbers in empty cells while ensuring the puzzle's constraints are met.

## Code Explanation

The solver follows these key steps:
- Find an empty cell (unassigned position).
- Try numbers 1-9 and check if they are valid in the current position.
- Recursively solve the rest of the puzzle.
- Backtrack if needed (if a number placement leads to an invalid solution).
- Print the solved Sudoku grid.
