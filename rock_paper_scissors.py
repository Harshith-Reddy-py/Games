import random

def get_user_choice():
    choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors'):
        print("You win!")
    elif (user == 'scissors' and computer == 'paper'):
        print("YOU WIN!")
    elif (user == 'paper' and computer == 'rock'):
        print("You win! ")
    else:
        print("Computer wins!") 

def play():
    print("\n\t---- Rock, Paper, Scissors Game ----")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(f"\"{result}\"")

while True :
    play()
    
