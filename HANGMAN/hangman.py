import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)                            # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()                                # what characters which user has guessed
    guess_times = min(len(word_letters) * 3, 15)        # how many times user is allowed to guess
    
    while guess_times > 0:
        # Shows how many times user is able to guess
        print("Guesses left: ", guess_times)
        # Shows what letters user has guessed
        print("You have used these letters: ", ' '.join(used_letters))
        # What the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        # User input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            guess_times = guess_times - 1               # decrease guess times
            used_letters.add(user_letter)               # add user guess word into list of used words
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                if len(word_letters) == 0:
                    print()
                    print("You won! You have guessed the word ", ' '.join([letter if letter in used_letters else '-' for letter in word]))
                    return
        elif user_letter in used_letters:
            print()
            print("You have guess this letter before! Try again.")
        else:
            print()
            print("Invalid character! Try again.")
        print()
    print("You lose! The word is", ' '.join([letter for letter in word]))
    return

if __name__ == '__main__':
    hangman()    