import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    
    print(" Welcome to Rock-Paper-Scissors Game ")
    
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print(" Invalid choice! Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f" Computer chose: {computer_choice}")
        
        winner = get_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("It's a Tie!")
        elif winner == "user":
            print(" You Win!")
            user_score += 1
        else:
            print(" Computer Wins!")
            computer_score += 1
        
        print(f" Score => You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(" Thanks for playing! Final Score => You:", user_score, "| Computer:", computer_score)
            break

play_game()
