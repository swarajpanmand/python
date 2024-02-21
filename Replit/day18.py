print("one-million-to-one")
number = 500000
while True:
  guess = int(input("What is your guess?: "))
  if guess < number:
    print("Too low")
  elif guess > number:
    print("Too high")
  elif guess == number:
    print("Correct")
    break
  else:
    print("That is not the number I am looking for")
    
  