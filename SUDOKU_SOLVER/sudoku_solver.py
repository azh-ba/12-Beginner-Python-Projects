import random

def check_unsafe(puzzle, value, row, col):
    """Check if the value is valid. Return True if yes."""
    # check values in the row
    for i in range(9):
        if puzzle[row][i] == value:
            return False
    
    # check values in the col
    for i in range(9):
        if puzzle[i][col] == value:
            return False
        
    # find row value of the block
    block_row_start = (row // 3)*3
    # find col value of the block
    block_col_start = (col // 3)*3
    # check values in the block
    for r in range(block_row_start, block_row_start + 3):
        for c in range(block_col_start, block_col_start + 3):
            if puzzle[r][c] == value:
                return False
    
    # value is safe
    return True

def check_empty(puzzle, row, col):
    """Check if the square is filled. Return True if yes."""
    if puzzle[row][col] == 0:
        return False
    return True

def next_empty_square(puzzle):
    """Return the next empty square."""
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    # no empty square existed        
    return None, None

def sudoku_backtracking(puzzle):
    """Solving sudoku using backtracking algorithm."""
    # find an empty square to fill in
    row, col = next_empty_square(puzzle)
    if row is None:
        return True
    
    # make a guess for the empty square
    for guess in range(1, 10):
        # if this is a valid guess --> fill in the value
        if check_unsafe(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # recursive call
            if sudoku_backtracking(puzzle):
                return True
        # not a valid guess | the guess does not solve --> backtrack and try a new number
        else:
            puzzle[row][col] = 0

    # if no number works --> puzzle is unsolvable
    return False

if __name__ == '__main__':
    puzzle = [
        [3, 9, 0,   0, 5, 0,    0, 0, 0],
        [0, 0, 0,   2, 0, 0,    0, 0, 5],
        [0, 0, 0,   7, 1, 9,    0, 8, 0],

        [0, 5, 0,   0, 6, 8,    0, 0, 0],
        [2, 0, 6,   0, 0, 3,    0, 0, 0],
        [0, 0, 0,   0, 0, 0,    0, 0, 4],

        [5, 0, 0,   0, 0, 0,    0, 0, 0],
        [6, 7, 0,   0, 0, 5,    0, 4, 0],
        [0, 0, 9,   0, 0, 0,    2, 0, 0]
    ]
    print(sudoku_backtracking(puzzle))
    for r in range(9):
        row = puzzle[r][0:9]
        print(' ' + ' '.join(str(row)) + ' ')
            