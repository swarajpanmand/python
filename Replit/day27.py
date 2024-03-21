
import random

def health():
  return ((random.randint(1,6))*(random.randint(1,12))/2 +10)

def strength():
  return ((random.randint(1,6))*(random.randint(1,12))/2 +12)

print("Character builder")
print()

while True:
  name = input("Name your legend: ")
  type = input("Character type (Human, Elf, Wizard, Orc): ")
  print()
  print(name)
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  print()
  again = input("Again?: ")
  if again == "yes":
    continue
  else:
    break