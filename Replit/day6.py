print("""
MY LOGIN SYSTEM
+++++++++++++++
""")

username = input("Username: ")
password = input("Password: ")

if username == "David" and password =="totallyNotBald":
  print("Why hello there David, what a lovely accent you have, you could have charmed your way in here even without a password.")
  print("Have a great day.")
  print("Don't forgot to wear a hat in the sun!")

elif username == "Suzanne" and password == "Su74nne":
  print("Hey there Suzanne!")

else:
  print("Go away!")