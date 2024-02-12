print("Hello World")
print("Select your move(R, P or S")
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
if player1 == "R" and player1 == "P":
  print("Player1's Rock is smothered by Player2's Paper!")
elif player1 == "R" and player2 == "S":
  print("Player2's Scissors is smothered by Player1's Rock!")
elif player1 == "P" and player2 == "R":
  print("Player2's Rock is smothered by Player1's Paper!")
elif player1 == "P" and player2 == "S":
  print("Player1's Paper is smothered by Player2's Scissors!")
elif player1 == "S" and player2 == "R":
  print("Player1's Scissors is smothered by Player2's Rock!")
elif player1 == "S" and player2 == "P":
  print("Player2's Paper is smothered by Player1's Scissors!")
else:
  print("Invalid Move")
