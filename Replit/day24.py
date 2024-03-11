import random
def dice(slides):
  diceroll = random.randint(1,slides)
  print("You rolled," , diceroll)
  print()
  again = input("Roll again? ")
  if again == "yes":
    dice(slides)
  else:
    return

slides = int(input("How many slides?: "))
dice(slides)