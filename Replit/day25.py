import random
print("CHARACTER STAT GENERATOR")

def character(n):
  for i in range(n):
    chara = input("Name your warrior: ")
    print("their health is", random.randint(1,6) * random.randint(1,8), "hp")
    print()

character(3)
  