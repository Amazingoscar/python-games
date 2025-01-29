import random

def play_game():
    options = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Ask for the user input
        user_choice = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break

        if user_choice not in options:
            print("Invalid choice! Please select Rock, Paper, or Scissors.")
            continue

        # Computer choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
