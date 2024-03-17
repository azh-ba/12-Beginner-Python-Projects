import os
import random

class Minesweeper:
    def __init__(self, row = None, col = None, mines = None):
        """Constructor of the game.
        self.row    int         row value
        self.col    int         col value
        self.board  list[][]    2D matrix contains value for the game
        """
        # assign default values for row, col, mines
        if (row == None) or (row < 5):
            self.row = 10
        else:
            self.row = row
        if (col == None) or (col < 5):
            self.col = 10
        else:
            self.col = col
        if (mines == None) or (mines >= (self.row*self.col)//2):
            self.mines = 10
        else:
            self.mines = mines

        # end-game condition
        self.win = None

    def generate_board(self):
        """Generate mines for the game."""
        # initialize the empty board; mines_list for storing mine coordinates
        self.board = [[' ' for _ in range(self.col)] for _ in range(self.row)]
        self.mines_row_list = []
        self.mines_col_list = []
        
        # generate mines for the board
        mine_placed = 0
        while mine_placed < self.mines:
            row_rand = random.randint(0, (self.row - 1))
            col_rand = random.randint(0, (self.col - 1))
            if self.board[row_rand][col_rand] == ' ':
                self.board[row_rand][col_rand] = 'X'
                self.mines_row_list.append(row_rand)
                self.mines_col_list.append(col_rand)
                mine_placed += 1

        # delete the 'X's 
        self.board = [[' ' for _ in range(self.col)] for _ in range(self.row)]

    def print_board(self):
        """Print the current state of the game."""
        # generate number list for coordinate visualization
        num_list = [str(x) for x in range(self.row)]
        print('    ' + '   '.join(num_list))
        print('___' + '_|__'.join('' for _ in range(self.row + 1)))

        # print the game 1 row at a time
        for r in range(self.row):
            print(f'{num_list[r]} | ' + ' | '.join(self.board[r]) + ' |')
    
    def print_board_end(self, row = None, col = None):
        """Print the final state of the game. 
        row, col    int     use only for highlighting the player's square.
        """
        # generate number list for coordinate visualization
        num_list = [str(x) for x in range(self.row)]
        print('    ' + '   '.join(num_list))
        print('___' + '_|__'.join('' for _ in range(self.row + 1)))

        # assign 'X's to the board
        for i in range(len(self.mines_row_list)):
            r = self.mines_row_list[i]
            c = self.mines_col_list[i]
            self.board[r][c] = 'X'

        # highlight the player-selected square that contains the mine
        if (row is not None) and (col is not None):
            self.board[row][col] = '#'

        # print the game 1 row at a time
        for r in range(self.row):
            print(f'{num_list[r]} | ' + ' | '.join(self.board[r]) + ' |')

    def valid_input(self, row, col):
        """Check if player input is valid. Return True if yes."""
        # row and col must not be null
        if row is None and col is None:
            return False
        
        # no out of bound location values
        if (row < 0) or (col < 0) or (row >= self.row) or (col >= self.col):
            return False
        
        # selected square has to be empty
        if self.board[row][col] != ' ':
            return False
        
        # satisfies all the conditions
        return True
    
    def check_mine(self, row, col):
        """Check if mine is existed in the location. Return True if yes."""
        for i in range(len(self.mines_row_list)):
            if (row == self.mines_row_list[i]) & (col == self.mines_col_list[i]):
                return True
        return False

    def check_empty(self):
        """Check if the board is empty. Return True if yes."""
        for row in range(self.row):
            for col in range(self.col):
                if self.board[row][col] == ' ':
                    return True
        return False
    
    def count_empty(self):
        """Return the number of empty squares left on the board."""
        count = 0
        for r in range(self.row):
            for c in range(self.col):
                if self.board[r][c] == ' ':
                    count += 1
        return count

    def assign_values(self, row, col):
        """Assign value to the square that the player chose.
        row, col    int     player's square coordinates
        """
        # base case: squares that are out of bound --> skip
        if (row < 0) or (col < 0) or (row >= self.row) or (col >= self.col):
            return
        # base case: squares that already have values --> skip
        elif (self.board[row][col] != ' ') or (self.check_mine(row, col)):
            return

        # check surrounding squares
        count = 0
        if self.check_mine(row - 1, col - 1):
           count += 1
        if self.check_mine(row - 1, col):
           count += 1
        if self.check_mine(row - 1, col + 1):
           count += 1
        if self.check_mine(row, col - 1):
           count += 1
        if self.check_mine(row, col + 1):
           count += 1
        if self.check_mine(row + 1, col - 1):
           count += 1
        if self.check_mine(row + 1, col):
           count += 1
        if self.check_mine(row + 1, col + 1):
           count += 1
        
        # base case: there is a mine nearby --> assign value
        if count != 0:
            self.board[row][col] = str(count)
        else:
            # recursively assign values to the nearby squares
            self.board[row][col] = '/'
            self.assign_values(row - 1, col - 1)
            self.assign_values(row - 1, col)
            self.assign_values(row - 1, col + 1)
            self.assign_values(row, col - 1)
            self.assign_values(row, col + 1)
            self.assign_values(row + 1, col - 1)
            self.assign_values(row + 1, col)
            self.assign_values(row + 1, col + 1)

def play(game):
    """Function for running the game."""
    game.generate_board()
    game.print_board()
    while (game.check_empty()) and (game.count_empty() > game.mines):
        row, col = None, None
        while ((row is None) and (col is None)) or (game.valid_input(row, col) == False):
            try:
                row, col = map(int, input("Choose a square: (row, col) ").split())
            except ValueError as ve:
                print("Invalid input! Try again.")
        if game.check_mine(row, col):       # player hits the mine
            print("You lose!")
            game.print_board_end(row, col)
            return
        else:
            game.assign_values(row, col)
            game.print_board()
    # board is left with only mine squares
    print("You won!")
    return

if __name__ == '__main__':
    """Default game is:
    row = 10 (must be higher than 5)
    col = 10 (must be higher than 5)
    mines = 10 (mines must be lower than (row*col)/2, else default value)
    """
    os.system('cls')
    game = Minesweeper(row = 10, col = 10, mines = 20)
    play(game)