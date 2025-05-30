def validateLogIn(passwordEntered):
  validPasswords = ("Atlantic35", "Pacific50", "Adriatic65")
  if passwordEntered in validPasswords:
    return 'Log-in successful'
  else:
    return 'Log-in failed'

userPasswordEntered = input('Enter your password: ')
print(validateLogIn(userPasswordEntered))