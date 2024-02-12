print("Exam Grade Calculator")
exam = input("Name of exam: ")
maxScore = int(input("Max. Possible Score: "))
yourScore = int(input("Your score: "))
percentage = yourScore / maxScore * 100
percentage= round(percentage,2)
if percentage >= 90:
  print("You got ", percentage,"% which is a A+")
elif percentage >= 80 and percentage <= 89:
  print("You got ", percentage,"% which is a A")
elif percentage >= 70 and percentage <= 79:
  print("You got ", percentage,"% which is a B")
elif percentage >= 60 and percentage <= 69:
  print("You got ", percentage,"% which is a C")
elif percentage >= 50 and percentage <= 59:
  print("You got ", percentage,"% which is a D")
else:
  print("You got ", percentage,"% which is a U")
