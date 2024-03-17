import os
import random

class Minesweeper:
    def __init__(self, row = None, col = None, mines = None):
        """Constructor of the game.
        self.row    int         row value
        self.col    int         col value
        self.board  list[][]    2D matrix contains value for the game
        """
        # assign default vlaues for row, col, mines
        if row == None:
            self.row = 10
        else:
            self.row = row
        if col == None:
            self.col = 10
        else:
            self.col = col
        if mines == None:
            self.mines = 10
        else:
            self.mines = mines
        self.lose = None

    def generate_board(self):
        """Generate mines for the game."""
        # initialize the empty board; mines_list for storing mine locations
        self.board = [[' ' for _ in range(self.col)] for _ in range(self.row)]
        self.mines_row_list = [self.row]
        self.mines_col_list = [self.col]
        
        # generate mines for the board
        mine_placed = 0
        while mine_placed < self.mines:
            row_rand = random.randint(0, (self.row - 1))
            col_rand = random.randint(0, (self.col - 1))
            if self.board[row_rand][col_rand] == ' ':
                #self.board[row_rand][col_rand] = 'X'
                self.mines_row_list.append(row_rand)
                self.mines_col_list.append(col_rand)
                mine_placed += 1

    def print_board(self):
        """Print the current state of the game."""
        # generate number list for coordinate visualization
        num_list = [str(x) for x in range(self.row)]
        print('    ' + '   '.join(num_list))
        print('___' + '_|__'.join('' for _ in range(self.row + 1)))
        # print the game 1 row at a time
        for r in range(self.row):
            print(f'{num_list[r]} | ' + ' | '.join(self.board[r]) + ' |')

    def check_mine(self, row, col):
        """Check if mine is existed in the location. Return True if yes."""
        for i in range(self.row):
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

    def assign_values(self, row, col):
        """Assign value to the square that the player chose.
        row     int     player's horizontal value
        col     int     player's vertical value
        """
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
        return str(count)

    def valid_input(self, row, col):
        """Check if player input is valid. Return True if yes."""
        if row is None and col is None:
            return False
        if self.board[row][col] != ' ':
            return False
        return True

def play(game):
    """Function for running the game."""
    game.generate_board()
    game.print_board()
    while game.check_empty():
        row, col = None, None
        while (row is None) and (col is None) or (game.valid_input(row, col) == False):
            try:
                row, col = map(int, input("Choose a square: (row, col) ").split())
            except ValueError as ve:
                print("Invalid input! Try again.")
        if game.check_mine(row, col):
            game.lose = True
            break
        else:
            game.board[row][col] = game.assign_values(row, col)
            game.print_board()
    if game.lose:
        print("You lose!")
    else:
        print("You won!")

if __name__ == '__main__':
    os.system('cls')
    game = Minesweeper()
    play(game)