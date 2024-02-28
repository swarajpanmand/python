print("Math Game!")
print()
count= 0
number = int(input("Name your multiples: "))
for i in range(1,11,1):
  print(i," x ",number,"=")
  answer = int(input())
  if answer == i*number:
    print("Great work!")
    count += 1
  else:
    print("Nope. The answer was " , i*number,".")
print("You scored ",count," out of 10.")