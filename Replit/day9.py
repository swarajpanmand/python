print("generation identifier")
year = int(input("which year were you born?"))
if year >= 1883 and  year <= 1900:
  print("lost generation")
elif year >= 1901 and year <= 1927:
  print("greatest generation")
elif year >= 1928 and year <= 1945:
  print("silent generation")
elif year >= 1946 and year <= 1964:
  print("baby boomers")
else:
  print("try again")