print("REPLIT LOGIN SYSTEM")
print()

def login():
  username = input("What is your username?: ")
  password = input("What is your password?: ")
  if username == "david" and password == "baldies4life":
    print("welcome to replit!!")
    return
  else:
    print("whoops! i dont recoginize that username or password, try again")
    login()

login()