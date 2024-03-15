import random
import math

class Player():
    def __init__(self, letter):
        """Constructor of the class.
        This is the parent class."""
        self.letter = letter
    
    def get_move(self):
        """Inheritance method."""
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        """Constructor of the class.
        This is the user's class."""
        super().__init__(letter)

    def get_move(self, game):
        """Return a valid move from the user."""

        # check if the move is valid
        valid = False
        while valid == False:
            square = int(input("Choose a empty square to make a move (0-8): "))
            try:
                if square not in game.empty_squares():
                    raise ValueError
                valid = True
            except ValueError:
                print("Invalid move. Try again.")
        return square
    

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        """Constructor of the class.
        This is the computer's class. This opponent makes move randomly."""
        super().__init__(letter)
    
    def get_move(self, game):
        """Return a random valid move from the computer."""
        square = random.choice(game.empty_squares())
        return square
    

class MinimaxComputerPlayer(Player):
    def __init__(self, letter):
        """Constructor of the class.
        This is the computer's class. This opponent uses Minimax algorithm to find the optimal move."""
        super().__init__(letter)

    def get_move(self, game):
        """Return the best possible move from the computer."""
        if game.num_empty_squares() == 9:
            square = random.choice(game.empty_squares())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, game, letter):
        """Recursively finding the optimal move from the current state."""
        # assign players to max and min role
        max_player = self.letter
        min_player = 'X' if max_player == 'O' else 'O'

        # base case: one of the player wins, or ends in tie
        if game.winner == max_player:
            return {'position': None, 'score': 1 * (game.num_empty_squares() + 1)}
        elif game.winner == min_player:
            return {'position': None, 'score': -1 * (game.num_empty_squares() + 1)}
        elif game.num_empty_squares() == 0:
            return {'position': None, 'score': 0}
        
        # setup
        if letter == max_player:
            best_move = {'position': None,
                    'score': -math.inf}
        else:
            best_move = {'position': None,
                    'score': math.inf}
            
        # loop through each possible moves
        for move in game.empty_squares():
            # 1. make a move
            game.make_move(move, letter)
            # 2. recurse to simulate the next state after making the move (alternate players)
            sim_move = self.minimax(game, min_player)
            # 3. undo the move on the board, and remove the winner if happened (because this is a simulated run, not the actual game)
            game.board[move] = ' '
            game.winner = None
            sim_move['position'] = move
            # 4. update result
            if letter == max_player:
                if sim_move['score'] > best_move['score']:
                    best_move = sim_move
            else:
                if sim_move['score'] < best_move['score']:
                    best_move = sim_move
        
        # return the best move
        return best_move