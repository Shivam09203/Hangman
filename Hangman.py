import random

# List of words to choose from
words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear']

def choose_word(words):
    """Choose a random word from the list."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with underscores for unguessed letters."""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    """Main function to play the Hangman game."""
    # Choose a word
    word = choose_word(words)
    # Initialize variables
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(display_word(word, guessed_letters))

    # Main game loop
    while True:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess! Attempts remaining:", attempts)
            if attempts == 0:
                print("You ran out of attempts! The word was:", word)
                break
        else:
            print("Correct guess!")

        # Display current state of the word
        display = display_word(word, guessed_letters)
        print(display)

        # Check if the word has been completely guessed
        if '_' not in display:
            print("Congratulations! You guessed the word:", word)
            break

# Play the game
hangman()
