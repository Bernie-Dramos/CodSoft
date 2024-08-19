# Calling needed libraries
import random

# Variable for scores
user_wins = 0
pc_wins = 0

# Store the options in a list
options= ["rock","paper", "scissors"]

# Checking input provided by user
while True:
    user_input = input("Choose Rock, Paper, Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    pc_choice = options[random_number]
    
    print("Computer choice was ", pc_choice + ".")
    
    if user_input == "rock" and pc_choice == "scissors":
        print("Rock smashes scissors! You win!")
        user_wins += 1
        
    elif user_input == "paper" and pc_choice == "rock":
        print("Paper covers rock! You win!")
        user_wins += 1     
    
    elif user_input == "scissors" and pc_choice == "paper":
        print("Scissors cuts paper! You win!")
        user_wins += 1
        
    elif user_input == pc_choice:
        print("It's a tie!")
    
    else:
        print("You lose this round!")
        pc_wins += 1
        continue
        
print("You won ", user_wins, "times.")
print("The computer won ", pc_wins, " times.")