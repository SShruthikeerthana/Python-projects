import random


RED = "\033[91m"
ORANGE = "\033[93m" 
GREEN = "\033[92m"
RESET = "\033[0m"

number_to_guess = random.randint(1, 100)
attempts = 0

print(" Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100... ")

while True:
    try:
        guess = int(input(" Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print(f"{ORANGE} Too low! Try again.{RESET}")
        elif guess > number_to_guess:
            print(f"{RED}Too high! Try again.{RESET}")
        else:
            print(f"{GREEN} \U0001F389 Congratulations! You guessed the number {number_to_guess} in {attempts} tries! 🏆{RESET}")
            break

        if abs(guess - number_to_guess) <= 5 and guess != number_to_guess:
            print(" You're very close!")

    except ValueError:
        print("\u26A0 Please enter a valid number.")
