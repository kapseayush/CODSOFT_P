import random


# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


# Function to get the user's choice
def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"


# Main function
def main():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thank you for playing!")


# Run the main function
if __name__ == "__main__":
    main()
