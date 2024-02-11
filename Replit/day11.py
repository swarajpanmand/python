min= 60
hour = 60 * min
day = 24 * hour
year= 365 * day
leap = int(input("is it a leap year? "))
if leap == 1:
  year= year + day

print(year)
  