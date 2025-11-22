
# hangman_game.py
import random

WORDS = ["apple", "tiger", "robot", "pizza", "dog"]

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("=== Simple Hangman Game ===")
    word = random.choice(WORDS)
    guessed_letters = set()
    attempts = 6

    print("Guess the word! It has", len(word), "letters.")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("\n Congratulations! You guessed the word:", word)
            return

    print("\n You lost! The word was:", word)

if __name__ == "__main__": 
    hangman()
