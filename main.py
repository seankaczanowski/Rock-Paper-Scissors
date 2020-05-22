"""
Rock Paper Scissors 1.0.1
Developed by Sean Kaczanowski
No Copyright
2018
"""

#Title Screen
print(" ")
print("+-------------------------+  ")
print("| Rock Paper Scissors 1.0 |  ") 
print("+-------------------------+  ")
print("                             ")
print("   ###     \~~~\     \/      ")
print("  ####      \___\    db      ")
print("                             ")
print("  + Press 'P' for Paper      ")
print("  + Press 'R' for Rock       ")
print("  + Press 'S' for Scissors   ")
print("  + Press 'X' to Exit        ")
print("  + Press 'Enter' to Play    ")
print(" ")

import random #For computer choice

# Game Loop
win = 0
lose = 0
i = 1
while i == 1:
  choice = input("Player Choice: ")

  if choice == "r" or choice == "R":
    play = "Rock"
  elif choice == "p" or choice == "P":
    play = "Paper"
  elif choice == "s" or choice == "S":
    play = "Scissors"
  else:
    print("Incorrect Input")
    play = "error"

  #Computer Choice
  rockpaperscissors = random.randint(1,3)

  if rockpaperscissors == 1:
    computer = "Rock"
  elif rockpaperscissors == 2:
    computer = "Paper"
  elif rockpaperscissors == 3:
    computer = "Scissors"
      
  #Different Outcomes
  if play == "error":
    print("Error\n")
      
  elif computer == "Rock" and play == "Rock":
    print("\nPlayer: Rock")
    print("Computer: Rock")
    print("Tie!\n")

  elif computer == "Rock" and play == "Paper":
    print("\nPlayer: Paper")
    print("Computer: Rock")
    print("You Win!\n")
    win += + 1

  elif computer == "Rock" and play == "Scissors":
    print("\nPlayer: Scissors")
    print("Computer: Rock")
    print("You Lose!\n")
    lose += + 1

  elif computer == "Paper" and play == "Rock":
    print("\nPlayer: Rock")
    print("Computer: Paper")
    print("You Lose!\n")
    lose += + 1

  elif computer == "Paper" and play == "Paper":
    print("\nPlayer: Paper")
    print("Computer: Paper")
    print("Tie!\n")

  elif computer == "Paper" and play == "Scissors":
    print("\nPlayer: Scissors")
    print("Computer: Paper")
    print("You Win!\n")
    win += + 1

  elif computer == "Scissors" and play == "Rock":
    print("\nPlayer: Rock")
    print("Computer: Scissors")
    print("You Win!\n")
    win =+ + 1

  elif computer == "Scissors" and play == "Paper":
    print("\nPlayer: Paper")
    print("Computer: Scissors")
    print("You Lose!\n")
    lose += + 1

  elif computer == "Scissors" and play == "Scissors":
    print("\nPlayer: Scissors")
    print("Computer: Scissors")
    print("Tie!\n")       

  elif option == "x" or "X":
    print("\nExiting Rock Paper Scissors 1.0") #Exit Message
    quit()

  
  print("Wins: " + str(win) + " Loses: " + str(lose))
  print("================")
  print(" ")