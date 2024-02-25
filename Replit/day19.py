print("Loan Calculator")
print()
print("$1000 over 10 years at 5% APR")
loan = 1000
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print("Year ", i+1, " is ", round(loan, 2))

print()
print("You paid $", round(loan-1000, 2)," in interest!")