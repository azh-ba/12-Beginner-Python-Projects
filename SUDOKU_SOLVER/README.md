**SUDOKU_SOLVER**

**Sudoku** is a logic-based, combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nin 3x3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contains all of the digits rom 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution. [Wikipedia](https://en.wikipedia.org/wiki/Sudoku)

There are several computer algorithms that will solve 9x9 puzzles (n = 9) in fractions of a second, but combinatorial explosion occurs as n incrases, creating limits to the properties of Sudokus that can be constructed, analyzed, and solved as n increases. [Wikipedia](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)

This project will implement backtracking, one of the algorithms (or methods) that can be used to solve a game of Sudoku.

> `sudoku_solver.py`: User feeds an unfinished game of sudoku into the function, to receive a possible solution, or none if the puzzle is unsolvable.

> `test.py`: This file is for testing various conditions.