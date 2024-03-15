import random

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