options = ['rock', 'paper', 'scissors']


def Players():
  player_1 = input("Player 1, Rock, Paper or Scissors: ").lower()
  player_2 = input("Player 2, Rock, Paper or Scissors: ").lower()
  if player_1 == player_2:
    print("It's a draw")
  if player_1 == options[0] and player_2 == options[1]:
    print("Player 2 wins!")
  elif player_1 == options[2] and player_2 == options[0]:
    print("Player 2 wins!")
  elif player_1 == options[1] and player_2 == options[2]:
    print("Player 2 wins!")
  else:
    print("Player 1 wins!")
  again = input("Want to play again?").lower()
  if again == "no":
    quit()
  elif again == "yes":
    Players()
  else:
    print("Invalid input, type 'yes' or 'no'")
  

#Main Program
Players()