votingAge = 18

userName = input("Enter name: ")
userAge = input("Enter age: ")
userInfo = userName + " " + userAge

if int(userAge) < votingAge:
  print(userInfo + " Sorry, you are not eligible to vote")
else:
  print(userInfo + " Proceed to the voting booth")
