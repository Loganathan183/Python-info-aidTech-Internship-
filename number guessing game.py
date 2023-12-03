import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100.")

    play_again = True

    while play_again:
        secret_number = random.randint(1, 100)
        attempts = 0

        while attempts < 10:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations, {name}! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        else:
            print(f"Sorry, {name}. You couldn't guess the number {secret_number} in 10 attempts. Game over!")

        play_again_input = input("Do you want to play again? (yes/no) ").lower()
        play_again = play_again_input == 'yes'

    print("Thanks for playing!")

if __name__ == "__main__":
    number_guessing_game()
