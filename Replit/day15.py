exit = ""

while exit != "yes":
  cow = input("waht animal do you want? : ")
  if cow == "cow":
    print("A cow goes moo. ")
  elif cow == "dog":
    print("a dog goes woof")
  elif cow == "cat":
    print("a cat goes meow")
  else:
    print("I don't know that animal")
  exit = input("do you want to exit? : ")