from player import HumanPlayer, MinimaxComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    @staticmethod
    def print_board_nums():
        number_board = [[f"{i}" for i in range(j*3, (j + 1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def print_board(self):
        for row in [self.board[i*3:(i + 1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_index = square // 3
        row = self.board[row_index*3:(row_index + 1)*3]
        if all(s == letter for s in row):
            return True
        
        # check column
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
            
        # no winning position
        return False

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']
    

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}.")
                game.print_board()
                print()
            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter
            letter = 'O' if letter == 'X' else 'X'
    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = MinimaxComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game = True)