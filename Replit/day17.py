print("MORE EPIC BATTLE")
p1 = 0
p2 = 0
p3 = 0

while True:
  print("Select your move(R, P or S)")
  player1 = input("Player 1 > ")
  player2 = input("Player 2 > ")
  if player1 == "R" and player1 == "P":
    print("Player1's Rock is smothered by Player2's Paper!")
    p2 += 1
  elif player1 == "R" and player2 == "S":
    print("Player2's Scissors is smothered by Player1's Rock!")
    p1 += 1
  elif player1 == "P" and player2 == "R":
    print("Player2's Rock is smothered by Player1's Paper!")
    p1 += 1
  elif player1 == "P" and player2 == "S":
    print("Player1's Paper is smothered by Player2's Scissors!")
    p2 += 1
  elif player1 == "S" and player2 == "R":
    print("Player1's Scissors is smothered by Player2's Rock!")
    p2 += 1
  elif player1 == "S" and player2 == "P":
    print("Player2's Paper is smothered by Player1's Scissors!")
    p1 += 1
  else:
    print("Invalid Move")

  if p1 == 3:
    print("Thanks for playing! player 1 wins!!")
    exit()
  elif p2 == 3:
    print("Thanks for playing! player 1 wins!!")
    exit()
  else:
    continue
