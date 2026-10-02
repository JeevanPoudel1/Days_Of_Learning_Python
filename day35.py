import random

# List of words
words = ["python", "computer", "programming", "keyboard", "internet"]

# Select a random word
word = random.choice(words)

# Game settings
attempts = 6
guessed_letters = []

print("================================")
print("      WORD GUESSING GAME")
print("================================")
print("Guess the hidden word!")
print(f"You have {attempts} attempts.")

# Main game loop
while attempts > 0:

    # Display the word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Attempts remaining:", attempts)

# Game over
if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)