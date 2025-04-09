secret_word = "tralalero tralala"
guesses = 0

print("Welcome to the word guessing game!")

while True:
        guess = input("What is your guess? ").lower()
        guesses += 1

        if guess == secret_word:
            print("Congratulations! You guessed it!")
            print(f"It took you {guesses} guesses.")
        else:
            print("Your guess was not correct.")