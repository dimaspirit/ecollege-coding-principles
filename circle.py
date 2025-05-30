from math import pow, pi
# Calculate the area of a circle (pi times the radius squared (A = π r²)).
#  The value for the radius should be entered by the user.
# Create a function called calculateAreaOfCircle() that performs the following tasks:
#  - Asks the user to enter the radius of a circle.
#  - Calculates the area of the circle.
#  - Prints the result to the console.

def calculateAreaOfCircle(radius):
  return pi * pow(radius, 2)

userInput = int(input("Enter a radius: "))
print("Area of the circle with radius", userInput, "is:", calculateAreaOfCircle(userInput))
  