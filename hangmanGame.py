import random


words = ["python", "hangman", "chatbot", "keyboard", "developer"]


def choose_word():
    return random.choice(words)


def display_state(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("=== Welcome to Hangman ===")
    print(f"Word has {len(word)} letters. You have {max_wrong} incorrect guesses allowed.\n")

    while wrong_guesses < max_wrong:
        print("Word: ", display_state(word, guessed_letters))
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.\n")

        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return

    
    print("You've run out of guesses!")
    print(f"The word was: {word}")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()