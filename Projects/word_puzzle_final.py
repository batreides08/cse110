"""
Author: Bryan Quiros
Purpose: To play a word puzzle game with the user 
"""


secret_word = "engineer"
guesses = 0

print("Welcome to the word guessing game!\n")

# Generate initial hint
print("Your hint is:", "_ " * len(secret_word))

while True:
    guess = input("What is your guess? ").lower()

    if len(guess) != len(secret_word):
        print("Your guess must be the same length as the secret word.")
        continue

    guesses += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guesses} guesses.")
        break

    # Generate hint
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "
        else:
            hint += "_ "

    print("Your hint is:", hint.strip())

