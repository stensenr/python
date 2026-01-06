import random

def get_choices():

   player_choice = input("Enter a choice (rock, paper, scissors): ")

   options = ["rock", "paper", "scissors"]
   computer_choice = random.choice(options)

   return check_win(player_choice, computer_choice)


def check_win(player, computer):

    print(f"You chose {player}, computer chose {computer}.")    

    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
          return "Computer wins!"        
    
 

print(get_choices())





