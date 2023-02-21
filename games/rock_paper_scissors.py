import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  if player == computer:
    print("It's a tie!")
  elif player == "rock":
    if computer == "paper":
      print("Player wins!")
    elif computer == "scissors":
      print("Computer wins!")
  elif player == "paper":
    if computer == "rock":
      print("Player wins!")
    elif computer == "scissors":
      print("Computer wins!")
  elif player == "scissors":
    if computer == "paper":
      print("Player wins!")
    elif computer == "rock":
      print("Computer wins!")
  return[player, computer]
  
choices = get_choices()
winner = check_win(choices["player"], choices["computer"])

print(choices)


