from player import HumanPlayer, RandomComputerPlayer, MinimaxComputerPlayer

class TicTacToe():
    def __init__(self):
        """Constructor of the class.

        board       list    the board of the game
        winner      char    the winner of the game"""
        self.board = [' ' for _ in range(9)]
        self.winner = None
    
    @staticmethod
    def num_board():
        """Print the number-coded board at the start of the game."""
        example_board = [[str(i) for i in range(j*3, (j + 1)*3)] for j in range(3)]
        for row in example_board:
            print('| ' + ' | '.join(row) + ' |')

    def print_board(self):
        """Print the current state of the game."""
        board = [self.board[i*3:(i + 1)*3] for i in range(3)]
        for row in board:
            print('| ' + ' | '.join(row) + ' |')

    def empty_squares(self):
        """Return a list of empty square's indexes."""
        return [i for i, x in enumerate(self.board) if x == ' ']
    
    def num_empty_squares(self):
        """Return the number of empty squares."""
        return self.board.count(' ')
        
    def make_move(self, square, letter):
        """Make the player's move to the chosen square. 
        Check if the move is valid.
        
        square      int     the square that the player wishes to place their letter in
        letter      char    the player associated with letter (x_player or o_player)
        """
        # place the letter in the square
        if self.board[square] == ' ':
            self.board[square] = letter
        # check if the move is winning
        if self.is_win(square, letter):
            self.winner = letter 

    def is_win(self, square, letter):
        """Check if a player is won after a move.
        
        square      int     the square which the player make a move on it
        letter      char    the player associated with letter (x_player or o_player)
        """
        # check row
        row_index = square // 3
        row = self.board[row_index*3:(row_index + 1)*3]
        if all(s == letter for s in row):
            return True
        
        # check col
        col_index = square % 3
        col = [self.board[col_index + i*3] for i in range(3)]
        if all(s == letter for s in col):
            return True
        
        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(s == letter for s in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(s == letter for s in diagonal2):
                return True
            
        # no winning
        return False
    

def play(game, x_player, o_player, print_game = True):
    """Main function to play the game.
    
    game            TicTacToe()     a instance of the TicTacToe game
    x_player        Player()        player that is assigned with 'X'
    o_player        Player()        player that is assigned with 'O'
    print_game      bool            print the game (or states). True if user wants to play, False if user wants to run many instances of the game
    """
    # print the game board
    if print_game:
        game.num_board()
        print()
        game.print_board()

    # set the player who will go first
    letter = 'X'

    while game.num_empty_squares() > 0:
        # determine which player will make the move  
        if letter == 'X':
            move = x_player.get_move(game)
            game.make_move(move, 'X')
            if print_game:
                print(f"X moves to square {move}.")
                game.print_board()
                print()
        elif letter == 'O':
            move = o_player.get_move(game)
            game.make_move(move, 'O')
            if print_game:
                print(f"O moves to square {move}.")
                game.print_board()
                print()
        else:
            print("Invalid move. Please try again.")
        
        # winner is found
        if game.winner == 'X':
            if print_game:
                print("X wins!")
            return letter
        elif game.winner == 'O':
            if print_game:
                print("O wins!")
            return letter
        
        # alternating turns between players 
        letter = 'O' if letter == 'X' else 'X'
    
    # winner is found
    if game.winner == 'X':
        if print_game:
            print("X wins!")
        return letter
    elif game.winner == 'O':
        if print_game:
            print("O wins!")
        return letter
        
    # no player wins
    if print_game:
        print("It's a tie!")
    return 'T'


def manual(bot, start_first = True):
    if start_first == True:
        x_player = HumanPlayer('X')
        o_player = bot
    else:
        x_player = bot
        o_player = HumanPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game = True)


def automatic(x_player, o_player, times):
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(times):
        game = TicTacToe()
        result = play(game, x_player, o_player, print_game = False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        elif result == 'T':
            ties += 1
    print(f"X won {x_wins} times ({(x_wins / times * 100):.2f}%).")
    print(f"O won {o_wins} times ({(o_wins / times * 100):.2f}%).")
    print(f"Ties {ties} times ({(ties / times * 100):.2f}%).")


if __name__ == '__main__':
    """Experiment section. Place desired Player type into manual() or automatic() function.
    
    manual()        human vs bot (Set start_first = False if user wants to go second)
    automatic()     bot vs bot"""
    rx = RandomComputerPlayer('X')
    ro = RandomComputerPlayer('O')
    mx = MinimaxComputerPlayer('X')
    mo = MinimaxComputerPlayer('O')

    x_player = mx
    o_player = mo
    manual(mo, start_first = True)
    #automatic(x_player, o_player, 500)