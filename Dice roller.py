import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def show_result(dice_values):
    print("Result:", ", ".join(map(str, dice_values)))

def dice_rolling_app():
    print("Welcome to the Dice Rolling App!")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            if num_dice <= 0:
                raise ValueError("Number of dice must be a positive integer.")
            break
        except ValueError as ve:
            print(f"Error: {ve}")

    while True:
        input("Press Enter to roll the dice...")
        dice_values = roll_dice(num_dice)
        show_result(dice_values)

        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for rolling the dice! Exiting the app.")
            break

if __name__ == "__main__":
    dice_rolling_app()
