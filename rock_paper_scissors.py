import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "user"
    return "computer"

def play_game():
    print("Rock, Paper, Scissors Game")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Your choice (rock, paper, scissors, or quit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print(f"You chose: {user_choice}, Computer chose: {computer_choice}")
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Scores - You: {user_score}, Computer: {computer_score}\n")

if __name__ == "__main__":
    play_game()
