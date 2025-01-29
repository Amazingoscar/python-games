import random

def play_number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        # Generate a random number between 1 and 20
        target_number = random.randint(1, 20)
        attempts = 3
        print("\nI'm thinking of a number between 1 and 20. You have 3 attempts to guess it!")

        while attempts > 0:
            # Get user's guess
            try:
                guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            # Check the guess
            if guess == target_number:
                print("🎉 Congratulations! You guessed the number!")
                break
            elif guess < target_number:
                print("Too low! Try guessing a higher number.")
            else:
                print("Too high! Try guessing a lower number.")
            
            attempts -= 1

        if attempts == 0 and guess != target_number:
            print(f"Sorry, you've run out of attempts! The number was {target_number}.")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_number_guessing_game()