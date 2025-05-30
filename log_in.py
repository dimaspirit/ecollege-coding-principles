passwords = ("Batman", "Robin", "Joker")

userPassword = input("Enter a password: ")

if userPassword in passwords:
  print("Password Validated")
else:
  print("Invalid password entered")
