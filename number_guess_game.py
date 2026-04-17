# number_guessing_game.py
# Number Guessing Game with Levels, Score, and Replay Option

import random

def play_game():
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("Choose difficulty level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        number = random.randint(1, 10)
        attempts = 5
    elif choice == "2":
        number = random.randint(1, 50)
        attempts = 7
    else:
        number = random.randint(1, 100)
        attempts = 10

    score = 0
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("✅ Congratulations! You guessed it right.")
            score += 10
            break
        elif guess < number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")
        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"❌ Game Over! The number was {number}.")
    print(f"Your Score: {score}")

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        play_game()

if __name__ == "__main__":
    play_game()
