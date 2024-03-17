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

    def generate_board(self):
        """Generate mines and related values for the game."""
        # initialize the empty board
        self.board = [[' ' for _ in range(self.col)] for _ in range(self.row)]
        row_list = [self.row]
        col_list = [self.col]
        
        # generate mines for the board
        mine_placed = 0
        while mine_placed < self.mines:
            row_rand = random.randint(0, (self.row - 1))
            col_rand = random.randint(0, (self.col - 1))
            if self.board[row_rand][col_rand] == ' ':
                self.board[row_rand][col_rand] = 'X'
                row_list.append(row_rand)
                col_list.append(col_rand)
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

    @staticmethod
    def print_empty_board(row, col):
        """Print the empty state of the game."""
        # generate empty_board
        empty_board = [[' ' for _ in range(col)] for _ in range(row)]
        # generate number list for coordinate visualization
        num_list = [str(x) for x in range(row)]
        print('    ' + '   '.join(num_list))
        print('___' + '_|__'.join('' for _ in range(row + 1)))
        # print the game 1 row at a time
        for r in range(row):
            print(f'{num_list[r]} | ' + ' | '.join(empty_board[r]) + ' |')

    def assign_values(self):
        """Assign values"""

def play():
    """Function for running the game."""
    os.system('cls')
    game = Minesweeper()
    game.generate_board()
    game.print_board()


if __name__ == '__main__':
    play()