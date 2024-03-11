import random

def computer_guess():
    # User prompting 2 numbers depicts the range of the game
    while True:
        try:
            low, high = map(int, input("I will guess the number in the range [low, high]: ").split())
            while low >= high:
                low, high = map(int, input("This range is not feasible. Try again: (low, high) ").split())
        except ValueError as ve:
            print("Must be two numbers separated by a whitespace! Try again!")
        else:
            break
    
    # Computer tries to guess the user's number
    while True:
        while low != high:
            random_number = random.randint(low, high)
            user_answer = input(f"Is {random_number} the right answer? (yes, high, low) ")
            if user_answer == 'high':
                high = random_number - 1
            elif user_answer == 'low':
                low = random_number + 1
            elif user_answer == 'yes':
                break
            else:
                user_answer = input(f"I cannot understand! Try again: (yes, high, low) ")
        if low == high:
            if user_answer == 'high':
                print(f"Number {random_number - 1} is the answer!")
                break
            elif user_answer == 'low':
                print(f"Number {random_number + 1} is the answer!")
                break
        else:
            print(f"Number {random_number} is the answer!")
            break
    
if __name__ == '__main__':
    computer_guess()