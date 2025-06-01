# The game will then generate a random number from 1 to 50 (inclusive). 
# The user enters a number from 1 to 50.
# The user’s entry must be compared to the random number. If it is less than the random number, the message ‘Too Low!’ should be printed to the console. If it is greater than the random number, the message ‘Too High!’ should be printed to the console. If it is equal to the random number, the message, ‘You Win!’ should be printed to the console. 
# The user is given 5 lives (five opportunities to guess the random number)

from random import randint

messageWelcome = "*** Welcome to 2Hig2Low game ***"
messageDescription = "The computer will generate a lucky number from 1-50 (inclusive). \n You must guess the lucky number! You have a 5 lives"
messageWish = "Good luck!"


luckyNumber = randint(1, 50)

print(messageWelcome)
print(messageDescription)
print(messageWish)

def tryGuess(lives):

  if(lives < 1):
    print("YOU LOOSE!")
    return

  print("Lives remaining:", lives)

  userGuess = int(input("Enter a number from 1 - 50: "))

  if(userGuess == luckyNumber):
    print("You WIN!")
    return

  if(userGuess > luckyNumber):
    print("Too High!")
    tryGuess(lives - 1)

  if(userGuess < luckyNumber):
    print("Too Low!")
    tryGuess(lives - 1)

tryGuess(5)
