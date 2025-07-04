import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within 1 and 100.")
                continue

            if guess < number:
                print("Too low. Try again!")
            elif guess > number:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
