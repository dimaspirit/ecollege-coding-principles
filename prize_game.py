winNumbers = (22, 46, 65)
userGuess = input("Enter a number from 1 - 100: ")

print("You entered " + userGuess)

if int(userGuess) in winNumbers:
  print("You have won a prize")
else:
  print("You have NOT won a prize")
