import random

def play():
    user = input("What is your choice? (rock, paper, scissors) ")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return f"It's a tie! I chose {computer} as well."
    if is_win(user, computer):
        return f"You won! I chose {computer}."
    return f"You lose! I chose {computer}."

def is_win(player, opponent):
    if (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock') or (player == 'rock' and opponent == 'scissors'):
        return True
    return False

if __name__ == '__main__':
    print(play())