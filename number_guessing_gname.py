import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Set the maximum number of attempts
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1  # Increment the attempts counter before the next iteration

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts!")
            break

    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry, you've run out of attempts! The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
