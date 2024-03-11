import random

def user_guess():
    # User prompting 2 numbers depicts the range of the game
    while True:
        try:
            low, high = map(int, input("Choose the range for the number: (low, high) ").split())
            while low >= high:
                low, high = map(int, input("This range is not feasible. Try again: (low, high) ").split())
        except ValueError as ve:
            print("Must be two numbers separated by a whitespace! Try again!")
        else:
            break
    
    # User guessing the number
    while True:
        try:
            random_number = random.randint(low, high)
            user_guess = int(input(f"Guess a number between {low} and {high}: "))
            while user_guess != random_number:
                if (user_guess > high) | (user_guess < low):
                    user_guess = int(input("This number is out of range! Guess again: "))
                elif user_guess > random_number:
                    user_guess = int(input("This number is higher than the target! Guess again: "))
                elif user_guess < random_number:
                    user_guess = int(input("This number is lower than the target! Guess again: "))
            print("You have guessed the number!")
        except ValueError as ve:
            print("Only accept numbers! Try again!")
        else: 
            break

if __name__ == '__main__':
    user_guess()