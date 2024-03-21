import os,time
n = 0
while(n!=1 and n!=2):
  print("Press 1 t Play")
  print("Press 2 to Exit")
  n=int(input("Enter your choice: "))
  if n==1:
    print("Playing some proper tunes!")
  elif n==2:
    exit()
  time.sleep(3)
  os.system("clear")
  n=0